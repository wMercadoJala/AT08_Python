from Pivotal.core.utils.project_helper import ProjectHelper


def before_feature(context, feature):
    if 'create_project' in feature.tags:
        context.project_id = ProjectHelper.create_project('Test create project')


def before_scenario(context, scenario):
    if 'create_webhook' in scenario.tags:
        ProjectHelper.create_webhook('https://elvillano.com')
