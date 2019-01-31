import json

from behave import *

from team_one_behave.core.logger.singleton_logger import SingletonLogger
from team_one_behave.core.rest_client.request_manager import *

logger = SingletonLogger().get_logger()


@step('I set up the project with the id "{id}"')
def step_impl(context, id):
    logger.info("Setting the id of the project")


@step("I set up the header")
def step_impl(context):
    context.client = RequestManager()
    header = json.loads(context.text)
    data = context.client.get_headers()
    for key in header.keys():
        data[key] = header[key]
    context.client.set_headers(data)
