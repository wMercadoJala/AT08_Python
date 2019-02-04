from team_one_behave.core.utils.common_helper import *
from team_one_behave.core.utils.project_helper import *


def before_scenario(context, scenario):
    if 'post_membership_account' in scenario.tags:
        CommonHelper.add_member()

    if 'create_project' in scenario.tags:
        ProjectHelper.create_project()

    if 'read_account' in scenario.tags:
        CommonHelper.get_account_id()


def after_scenario(context, scenario):
    if 'delete_data' in scenario.tags:
        CommonHelper.delete_member()
