# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = [["Station","Year","Month","Day","Hour","Max Load"]]
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    for i in range(1,9):
        name = sheet.cell_value(0,i)
        col = sheet.col(i,1,sheet.nrows)
        max_load = max(col)
        max_index = col.index(max_load) + 1
        max_load = max_load.value
        time = xlrd.xldate_as_tuple(sheet.cell_value(max_index,0),0)
        row = [name] + list(time) + [max_load]
        data.append(row)        
    return data

def save_file(data, filename):
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        for r in data:
            writer.writerow(r)
    csvfile.close()

    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024",
                        'Year': "2013",
                        "Month": "6",
                        "Day": "26",
                        "Hour": "17"}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line["Station"]
            if station == 'FAR_WEST':
                for field in fields:
                    assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Check Station Names
        assert set(stations) == set(correct_stations)
        
        # Output should be 8 lines not including header
        assert number_of_rows == 8
        
    print "All tests passed"

        
if __name__ == "__main__":
    test()
