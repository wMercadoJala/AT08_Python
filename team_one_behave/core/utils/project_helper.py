import json
import random
import string

from definitions import all_id
from team_one_behave.core.rest_client.request_manager import *


class ProjectHelper():

    @staticmethod
    def create_project():
        client = RequestManager()
        project_name = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        client.set_method("POST")
        client.set_endpoint("/projects")
        body = {"name": project_name}
        client.set_body(json.dumps(body))
        response = client.execute_request()
        all_id['project_id'] = response.json()['id']
