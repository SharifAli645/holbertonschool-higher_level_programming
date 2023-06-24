#!/usr/bin/python3
"""
Script that adds
arguments
to a
Python list
"""


import sys
import json
s_json = __import__('5-save_to_json_file').save_to_json_file
l_json = __import__('6-load_from_json_file').load_from_json_file


f_name = 'add_item.json'
i = 1

try:
    lista = l_json(f_name)
except BaseException:
    lista = list()

while i < len(sys.argv):
    lista.append(sys.argv[i])
    i = i + 1

s_json(lista, f_name)
