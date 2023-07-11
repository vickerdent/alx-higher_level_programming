#!/usr/bin/python3
"""Makes a list from args and saves them to a file in json format"""
import sys
savejson = __import__("5-save_to_json_file").save_to_json_file
loadjson = __import__("6-load_from_json_file").load_from_json_file

try:
    new_list = loadjson("add_item.json")
except FileNotFoundError:
    new_list = []
for arg in sys.argv[1:]:
    new_list.append(arg)
savejson(new_list, "add_item.json")