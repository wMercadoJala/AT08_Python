from Pivotal.core.utils.storage import Storage

container_id = Storage.get_instance()


def get_filter(param):
    path = param
    while path.find("$") >= 0:
        path_preview = path[str(path).find("$"):]
        key = path_preview[0:None if str(path_preview).find("/") == -1 else str(path_preview).find("/")]
        path = path.replace(key, str(container_id.get_value(key)))
    return path
