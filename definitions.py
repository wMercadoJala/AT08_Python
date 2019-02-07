import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMAS = {
    'Account': os.path.join(ROOT_DIR, 'Pivotal/schemas/account.schema.json'),
    'Project': os.path.join(ROOT_DIR, 'Pivotal/schemas/projects.schema.json')
}
