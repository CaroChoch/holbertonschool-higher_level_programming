#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file.
"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"
with open(filename, 'a+') as file:
    my_list = []
    my_list.extend(args[1:])
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
