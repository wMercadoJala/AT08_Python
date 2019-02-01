import random
import string
import json
from team_one_behave.core.rest_client.request_manager import *


class ProjectHelper():
    @staticmethod
    def create_project():
        client = RequestManager()
        project_name = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        client.set_method("POST")
        client.set_endpoint("/projects")
        # body = {"name": project_name}
        # body = """{"name": "{0}"}""".format(project_name)
        body = {"name": project_name}
        client.set_body(json.loads(str(body)))
        print(client.get_body())
        response = client.execute_request()
        print(response.json())


ProjectHelper.create_project()
