from Pivotal.core.utils.project_helper import ProjectHelper


def before_all(context):
    print("****************** PIVOTAL TRACKER API TESTING **************")


def before_feature(context, feature):
    if 'create_project' in feature.tags:
        context.project_id = ProjectHelper.create_project('project.dateTime')
    if 'accounts' in feature.tags:
        ProjectHelper.set_account_data()


def before_scenario(context, scenario):
    if 'create_webhook' in scenario.tags:
        ProjectHelper.create_webhook('https://elvillano.com')
    if 'create_membership' in scenario.tags:
        ProjectHelper.create_membership(405)
    if 'create_integration' in scenario.tags:
        ProjectHelper.create_integration("https://elrincondejira2.atlassian.net")
    if 'create_epic' in scenario.tags:
        ProjectHelper.create_epic('First epic to my project')


def after_all(context):
    ProjectHelper.clear_account()
    ProjectHelper.clear_account_memberships()
