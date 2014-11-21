import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col) 
                for col in range(sheet.ncols)] 
                    for r in range(sheet.nrows)]

    print "\nList Comprehension"
    print "data[3][2]:",
    print data[3][2]

    print "\nCells in a nested loop:"    
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print sheet.cell_value(row, col),


    ### other useful methods:
    print "\nROWS, COLUMNS, and CELLS:"
    print "Number of rows in the sheet:", 
    print sheet.nrows
    print "Type of data in cell (row 3, col 2):", 
    print sheet.cell_type(3, 2)
    print "Value in cell (row 3, col 2):", 
    print sheet.cell_value(3, 2)
    print "Get a slice of values in column 3, from rows 1-3:"
    print sheet.col_values(3, start_rowx=1, end_rowx=4)

    print "\nDATES:"
    print "Type of data in cell (row 1, col 0):", 
    print sheet.cell_type(1, 0)
    exceltime = sheet.cell_value(1, 0)
    print "Time in Excel format:",
    print exceltime
    print "Convert time to a Python datetime tuple, from the Excel float:",
    print xlrd.xldate_as_tuple(exceltime, 0)

    return data

data = parse_file(datafile)