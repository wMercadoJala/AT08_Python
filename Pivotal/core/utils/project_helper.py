import json

from Pivotal.core.rest_client.request_manager import RequestManager
from Pivotal.core.utils.storage_id import storage_id

container_id = storage_id.get_instance()


class ProjectHelper:
    id_project = None
    id_webhook = None

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
        container_id.add_value("$PROJECT_ID", response.json()['id'])
        ProjectHelper.id_project = response.json()['id']

    @staticmethod
    def create_webhook(name):
        client = RequestManager()
        body = {
            'webhook_url': name,
            'webhook_version': 'v5'
        }
        client.set_method('POST')
        client.set_endpoint('/projects/' + str(ProjectHelper.id_project) + '/webhooks')
        client.set_body(json.dumps(body))
        response = client.execute_request()
        container_id.add_value("$WEBHOOK_ID", response.json()['id'])
        ProjectHelper.id_webhook = response.json()['id']
