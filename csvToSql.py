import csv
import sys

filename = 'input.csv'
output_name = 'out.sql'
db_name = 'table'

#This function prints the first command of the SQL file (INSERT INTO db_name (column1, column2...)
#It gets the column1, column2, ..., columnN from
def printHeader(columns):
    print 'INSERT INTO `'+db_name+'` (',
    for field in columns:
        if field == columns[-1]:
            print '`' + field + '`) VALUES'
        else:
            print '`' + field + '`,',

# This function check each one of the columns with data and prints the insert command
# Ex: ('data1, 'data2', 'data3', ...., 'dataN'),
def printData(data):
    for row in data:
        print '(',
        for field in row:
            if field == row[-1]:
                print "'" + field + "' ,",
            else:
                print "'" + field + "'",
        print '),'

sys.stdout = open(output_name, 'w')
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    columns = next(reader)

    printHeader(columns)
    printData(reader)
