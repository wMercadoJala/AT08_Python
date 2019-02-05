# -*- coding: utf-8 -*-
class id_storage:

    container = None;
    our_instance = None;
    @staticmethod
    def get_instance():
        if (id_storage.our_instance == None):
            ourInstance = id_storage()
        return ourInstance;

    def __init__(self):
        id_storage.container = {}

    def add_value(self, key, value):
        id_storage.container[key] = value

    def get_value(self, key):
        return id_storage.container.get(key)

    def remove_value(self, key):
        del id_storage.container[key]
