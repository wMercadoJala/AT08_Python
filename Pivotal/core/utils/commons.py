from Pivotal.core.utils.id_storage import id_storage

container_id = id_storage.get_instance()

def get_filter(param):
    walk = 0
    ruta = param
    while ruta.find("$") >= 0:
        ruta_preview = ruta[str(ruta).find("$"):]
        key = ruta_preview[0:None if str(ruta_preview).find("/") == -1 else str(ruta_preview).find("/")]
        ruta = ruta.replace(key, str(container_id.get_value(key)))
        walk =+ 1
    return ruta
