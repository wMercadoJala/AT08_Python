# -*- coding: utf-8 -*-
class names_storage:

    container = None;
    ourInstance = None;
    @staticmethod
    def get_instance():
        if (names_storage.ourInstance == None):
            ourInstance = names_storage()
        return ourInstance;


    def __init__(self):
        names_storage.container = {}

    def addName(self, key, value):
        names_storage.container[key] = value
    def getName(self, key):
        return names_storage.container.get(key)

# algo = names_storage().get_instance()
#
# algo.addName("mono", "macaco")
# varchar = algo.getName("mono")
# print(varchar)