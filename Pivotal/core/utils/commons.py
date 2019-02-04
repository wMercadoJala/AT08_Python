from datetime import datetime

from Pivotal.core.utils.names_storage import names_storage

container = names_storage().get_instance()

def get_new_unique_name(text):
    return str(text).replace("dateTime", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]) if str(text).find("dateTime") >= 0 else str(text)


def get_filter(param):
    if str(param).find("$[") >= 0:
        value_to_replace = str(param)[str(param).find("{:"):str(param).find(":}") + 2]
        return str(param).replace(value_to_replace,container.getName(str(param)[str(param).find("{:")+2:str(param).find(":}")]))
    else:
        return param
