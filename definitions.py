import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMA_CREATION = os.path.join(ROOT_DIR, 'Pivotal/schemas/account.schema.Pivotal.json')
SCHEMAS = {
    'Project': os.path.join(ROOT_DIR, 'Pivotal/schemas/projects.schema.json')
}
