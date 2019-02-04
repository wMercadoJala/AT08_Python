"""Module for set the environment of behave"""
from team_one_behave.core.utils.common_helper import CommonHelper
from team_one_behave.core.utils.project_helper import ProjectHelper


def before_scenario(scenario):
    """
    Method who run before the scenario.
    :param scenario: Input scenario.
    """
    if 'post_membership_account' in scenario.tags:
        CommonHelper.add_member()

    if 'create_project' in scenario.tags:
        ProjectHelper.create_project()

    if 'read_account' in scenario.tags:
        CommonHelper.get_account_id()


def after_scenario(scenario):
    """
    Method who run after the scenario.
    :param scenario: Input scenario.
    """
    if 'delete_data' in scenario.tags:
        CommonHelper.delete_member()
