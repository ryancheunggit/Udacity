#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import math

def skip_lines(input_file, n):
    for i in range(n):
        input_file.next()

def is_number(v):
    try:
        ret = float(v)
    except:
        ret = None
    return ret

def ensure_float(v):
    if is_number(v):
        return float(v)

def audit_population_density(input_file):
    for row in input_file:
        population = ensure_float(row['populationTotal'])
        area = ensure_float(row['areaLand'])
        population_density = ensure_float(row['populationDensity'])
        if population and area and population_density:
            calculated_density = population / area
            if math.fabs(calculated_density - population_density) > 10:
                print "Possibly bad population density for ", row['name']

if __name__ == '__main__':
    input_file = csv.DictReader(open('cities.csv'))
    skip_lines(input_file, 3)
    audit_population_density(input_file)
