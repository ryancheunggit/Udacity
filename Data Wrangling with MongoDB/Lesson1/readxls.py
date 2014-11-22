#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min and max values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

# os.chdir('C:\Users\Violetta_Chen\Documents\GitHub\Udacity\Data Wrangling with MongoDB\Lesson1')


import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    coast_values = sheet.col_values(1,1)
    min_coast = min(coast_values)
    max_coast = max(coast_values)
    min_time = xlrd.xldate_as_tuple(sheet.cell_value(coast_values.index(min_coast)+1,0),0)
    max_time = xlrd.xldate_as_tuple(sheet.cell_value(coast_values.index(max_coast)+1,0),0)
    (min_time, 0)
    data = {}
    data['maxtime'] = max_time
    data['maxvalue'] = max_coast
    data['mintime'] = min_time
    data['minvalue'] = min_coast
    data['avgcoast'] = sum(coast_values)/len(coast_values)
   
    #data = {
    #        'maxtime': (0, 0, 0, 0, 0, 0),
    #        'maxvalue': 0,
    #        'mintime': (0, 0, 0, 0, 0, 0),
    #        'minvalue': 0,
    #        'avgcoast': 0
    #}
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()