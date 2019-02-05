from Pivotal.core.utils.project_helper import ProjectHelper


def before_feature(context, feature):
    if 'create_project' in feature.tags:
        context.project_id = ProjectHelper.create_project('Test create project')


def before_scenario(context, scenario):
    if 'create_webhook' in scenario.tags:
        ProjectHelper.create_webhook('https://elvillano.com')
    if 'create_membership' in scenario.tags:
        ProjectHelper.create_membership(405)

#
def before_all(context):
        print("****************** PIVOTAL TRACKER API TESTING **************")


def before_feature(context, feature):
    if 'smoke' in feature.tags:
        print("****************** SMOKE TESTS **************")

    elif 'acceptance' in feature.tags:
        print("****************** ACCEPTANCE TESTS **************")
