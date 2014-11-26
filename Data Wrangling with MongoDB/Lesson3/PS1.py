#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then
clean it up. In the first exercise we want you to audit the datatypes that can be found in some
particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a set of the datatypes
that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal",
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long",
          "areaLand", "areaMetro", "areaUrban"]

def skip_lines(input_file, skip):
    for i in range(skip):
        next(input_file)

def is_int(v):
    try:
        int(v)
        return True
    except ValueError:
        return False

def is_float(v):
    try:
        float(v)
        return True
    except ValueError:
        return False

def audit_file(filename, fields):
    fieldtypes = {}
    for field in fields:
        fieldtypes[field] = set()
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        skip_lines(reader,3)
        for row in reader:
            for field in fields:
                v = row[field]
                if v == "NULL" or v == "":
                    fieldtypes[field].add(type(None))
                elif v.startswith('{'):
                    fieldtypes[field].add(type([]))
                elif is_int(v):
                    fieldtypes[field].add(type(1))
                elif is_float(v):
                    fieldtypes[field].add(type(1.1))
                else:
                    fieldtypes[field].add(type('1.1'))
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1),type([]), type(None)])

if __name__ == "__main__":
    test()
