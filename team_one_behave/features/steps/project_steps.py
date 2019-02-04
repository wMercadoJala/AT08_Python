"""Module of steps for project"""
import json

from behave import step

from team_one_behave.core.logger.singleton_logger import SingletonLogger

LOGGER = SingletonLogger().get_logger()


@step("I set up the header")
def set_up_header(context):
    """
    Step for set the header of the request.
    :param context: Input context.
    """
    LOGGER.info("Add Headers to request")
    header = json.loads(context.text)
    data = context.client.get_headers()
    for key in header.keys():
        data[key] = header[key]
    context.client.set_headers(data)
