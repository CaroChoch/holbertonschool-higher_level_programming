#!/usr/bin/python3
""" Class Base """

import json


class Base:
    """
    Class Base : private class attribute
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all the future classes and
    to avoid duplicating the same code
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """

        my_list = []

        if list_objs is not None:
            for i in list_objs:
                my_list.append(i.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as file:
            file.write(cls.to_json_string(my_list))
