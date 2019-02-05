import json

from Pivotal.core.rest_client.request_manager import RequestManager


class ProjectHelper:
    @staticmethod
    def create_project(name):
        client = RequestManager()
        body = {
            'name': name,
            'new_account_name': 'Test account'
        }
        client.set_method('POST')
        client.set_endpoint('/projects')
        client.set_body(json.dumps(body))
        response = client.execute_request()
        print(response.json()['id'])
