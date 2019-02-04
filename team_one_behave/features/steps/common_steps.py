"""Module of Common steps"""
import json

from behave import step, then
from compare import expect
from jsonschema import validate

from definitions import SCHEMA_TODOLY
from team_one_behave.core.logger.singleton_logger import SingletonLogger
from team_one_behave.core.rest_client.request_manager import RequestManager
from team_one_behave.core.utils.common_helper import CommonHelper

LOGGER = SingletonLogger().get_logger()


@step(u'I set up a "{method}" request to "{endpoint}" endpoint')
def set_up_request_to_endpoint(context, method, endpoint):
    """
    Set up a request to an endpoint.
    :param context: Input context.
    :param method: Input method.
    :param endpoint: Input endpoint.
    """
    LOGGER.info("Make the call")
    client = RequestManager()
    client.set_method(method)
    client.set_endpoint(CommonHelper.read_endpoint(endpoint))
    context.client = client


@then(u'I get a "{status_code}" status code as response')
def get_status_code(context, status_code):
    """
    Verification of status code
    :param context: Input context.
    :param status_code: Input status code.
    """
    LOGGER.info("Validation Status Code")
    expect(int(status_code)).to_equal(context.response.status_code)


@step(u'I send the request')
def send_request(context):
    """
    Send the request.
    :param context: Input context.
    """
    LOGGER.info("Execute request")
    context.response = context.client.execute_request()


@step(u'I set up the data')
def set_up_body(context):
    """
    Setting the data.
    :param context: Input context.
    """
    LOGGER.info("Add Data to request")
    context.sent_data = context.text
    body = json.loads(context.sent_data)
    context.client.set_body(json.dumps(body))


@step("I validate with an schema")
def schema_validation(context):
    """
    Schema validation.
    :param context: Input context.
    """
    LOGGER.info("Validation of the schema")
    with open(SCHEMA_TODOLY['Creation']) as schema_creation:
        schema = json.load(schema_creation)
    validate(instance=context.response.json(), schema=schema)


@step("I verify the sent data")
def validation_sent_data(context):
    """
    Veridication of the sent data.
    :param context: Input context.
    """
    LOGGER.info("Validation of sent data")
    sent_json = json.loads(context.sent_data)
    for item in sent_json:
        response = context.response.json()
        expect(sent_json[item]).to_equal(response[item])
