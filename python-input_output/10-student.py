#!/usr/bin/python3
""" class Student that defines a student by: first_name, last_name, age """


class Student:
    """ Class Student that defines a student : public instance attributes """
    def __init__(self, first_name, last_name, age):
        """ Initializes a Student instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary representation of
        a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for element in attrs:
                if hasattr(self, element):
                    my_dict[element] = getattr(self, element)
            return my_dict
