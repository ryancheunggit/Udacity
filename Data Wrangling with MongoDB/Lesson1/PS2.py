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
    data = []
    ncol = sheet.ncols
    for i in range(1,ncol-1):
        d = {}
        d["Station"] = sheet.cell_value(0, i)
        colum_values = sheet.col_values(i, 1)
        maxload = max(colum_values)
        d["Max Load"] = maxload
        maxpos = colum_values.index(maxload)
        maxload_exceltime = sheet.cell_value(maxpos+1,0)
        maxload_time = xlrd.xldate_as_tuple(maxload_exceltime, 0)
        d["Year"] = maxload_time[0]
        d["Month"] = maxload_time[1]
        d["Day"] = maxload_time[2]
        d["Hour"] = maxload_time[3]
        
        data.append(d)
    return data

def save_file(data, filename):
    with open(filename, "wb") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter="|")
        writer.writeheader()
        writer.writerows(data)
    f.close()

    
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
