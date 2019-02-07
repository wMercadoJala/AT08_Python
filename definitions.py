import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

SCHEMA_CREATION = {
    'Account': os.path.join(ROOT_DIR, 'Pivotal/schemas/account.schema.json'),
}
