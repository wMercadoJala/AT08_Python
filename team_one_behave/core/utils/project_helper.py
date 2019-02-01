# from team_one_behave.core.rest_client.request_manager import *
import random
import string


class ProjectHelper():
    @staticmethod
    def create_project(context):
        # client = RequestManager()
        project_name = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        # client.set_method(GET)
        # client.set_endpoint(endpoint)

