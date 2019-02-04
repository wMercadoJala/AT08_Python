import json
import re

import yaml

from definitions import ENV_YML
from definitions import all_id
from team_one_behave.core.rest_client.request_manager import RequestManager

config_data = yaml.load(open(ENV_YML))


class CommonHelper():

    @staticmethod
    def read_endpoint(endpoint):
        if not re.search('{(.+?)}', endpoint):
            return endpoint
        read = re.findall('{(.+?)}', endpoint)
        result = endpoint
        for item in read:
            result = re.sub('{(%s)}' % item, str(all_id[item]), result)
        return result

    @staticmethod
    def get_account_id():
        all_id["account_id"] = config_data['account_id']
        all_id["member_id"] = config_data['member_id']

    @staticmethod
    def add_member():
        client = RequestManager()
        client.set_method("POST")
        client.set_endpoint("/accounts/{0}/memberships".format(config_data['account_id']))
        body = {"person_id": config_data['member_id']}
        client.set_body(json.dumps(body))
        client.execute_request()

    @staticmethod
    def delete_member():
        client = RequestManager()
        client.set_method("DELETE")
        client.set_endpoint("/accounts/{0}/memberships/{1}".format(config_data['account_id'], config_data['member_id']))
        client.execute_request()
