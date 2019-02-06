import json

from Pivotal.core.rest_client.request_manager import RequestManager
from Pivotal.core.utils import commons
from Pivotal.core.utils.storage import Storage

container_id = Storage.get_instance()


class ProjectHelper:
    project_id = None
    webhook_id = None
    membership_id = None
    epic_id = None

    @staticmethod
    def create_project(name):
        client = RequestManager()
        body = {
            'name': commons.get_unique_name(name),
            'project_type':'public'
        }
        client.set_method('POST')
        client.set_endpoint('/projects')
        client.set_body(json.dumps(body))
        response = client.execute_request()
        container_id.add_value("$PROJECT_ID", response.json()['id'])
        ProjectHelper.project_id = response.json()['id']
        return response.json()['id']

    @staticmethod
    def create_webhook(name):
        client = RequestManager()
        body = {
            'webhook_url': name,
            'webhook_version': 'v5'
        }
        client.set_method('POST')
        client.set_endpoint('/projects/' + str(ProjectHelper.project_id) + '/webhooks')
        client.set_body(json.dumps(body))
        response = client.execute_request()
        container_id.add_value("$WEBHOOK_ID", response.json()['id'])
        ProjectHelper.webhook_id = response.json()['id']

    @staticmethod
    def create_membership(person_id):
        client = RequestManager()
        body = {
            'person_id':person_id,
            'role':'member'
        }
        client.set_method('POST')
        client.set_endpoint('/projects/' + str(ProjectHelper.project_id) + '/memberships')
        client.set_body(json.dumps(body))
        response = client.execute_request()
        container_id.add_value("$MEMBERSHIP_ID_FOR_PROJECT", response.json()["id"])
        ProjectHelper.membership_id = response.json()['id']

    @staticmethod
    def create_integration(url):
        client = RequestManager()
        body = {
            'api_username':'fakeuser',
            'api_password': 'fakepassword',
            'filter_id': '474748',
            'base_url': url,
            'name': 'algointeresantee',
            'type': 'jira'
        }
        client.set_method('POST')
        client.set_endpoint('/projects/' + str(ProjectHelper.project_id) + '/integrations')
        client.set_body(json.dumps(body))
        response = client.execute_request()
        container_id.add_value("$INTEGRATION_ID", response.json()["id"])
        ProjectHelper.membership_id = response.json()['id']
