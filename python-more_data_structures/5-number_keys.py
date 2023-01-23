#!/usr/bin/python3


def number_keys(a_dictionary):
    nb_keys = 0
    for key,value in a_dictionary.items():
        nb_keys += 1
    return nb_keys
