# -*- coding: utf-8 -*-
class storage_id:

    container = None;
    our_instance = None;
    @staticmethod
    def get_instance():
        if (storage_id.our_instance == None):
            ourInstance = storage_id()
        return ourInstance;

    def __init__(self):
        storage_id.container = {}

    def add_value(self, key, value):
        storage_id.container[key] = value

    def get_value(self, key):
        return storage_id.container.get(key)

    def remove_value(self, key):
        del storage_id.container[key]
