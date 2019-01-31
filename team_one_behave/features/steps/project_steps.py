import json

from behave import *
from compare import *
from jsonschema import validate

from definitions import SCHEMA_CREATION
from team_one_behave.core.logger.singleton_logger import SingletonLogger
from team_one_behave.core.rest_client.request_manager import *
from team_one_behave.core.utils.json_helper import JsonHelper

logger = SingletonLogger().get_logger()


@step(u'I set up a "{method}" request to "{endpoint}" endpoint')
def step_impl(context, method, endpoint):
    logger.info("Make the call")
    # client = RequestManager()
    print("Header of the put", context.client.get_headers())
    context.client.set_method(method)
    context.client.set_endpoint(endpoint)
    # context.client = client


@then(u'I get a "{status_code}" status code as response')
def step_impl(context, status_code):
    logger.info("Validation Status Code")
    JsonHelper.print_pretty_json(context.response.json())
    expect(int(status_code)).to_equal(context.response.status_code)


@step(u'I set up a retrieve of all Projects')
def step_impl(context):
    logger.info("Make the call: ")
    client = RequestManager()
    client.set_method('GET')
    client.set_endpoint('/projects.json')
    context.client = client


@then(u'I get an OK response')
def step_impl(context):
    logger.info("Validation Smoke")
    JsonHelper.print_pretty_json(context.response.json())
    expect(200).to_equal(context.response.status_code)


@step(u'I send the request')
def step_impl(context):
    logger.info("Execute request")
    context.response = context.client.execute_request()


@step(u'I set up the data')
def step_impl(context):
    logger.info("Add Data to request")
    context.sent_data = context.text
    body = json.loads(context.sent_data)
    context.client.set_body(json.dumps(body))


@step("I validate with an schema")
def step_impl(context):
    logger.info("Validation of the schema")
    with open(SCHEMA_CREATION) as schema_creation:
        schema = json.load(schema_creation)
    validate(instance=context.response.json(), schema=schema)


@step("I verify the sent data")
def step_impl(context):
    logger.info("Validation of sent data")
    sent_json = json.loads(context.sent_data)
    for item in sent_json:
        response = context.response.json()
        expect(sent_json[item]).to_equal(response[item])
