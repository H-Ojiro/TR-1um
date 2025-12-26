#! /usr/bin/env python3
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# TR-1um DRC v0.001 
# Original version was made by jun1okamura from TokaiRika's document 
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- 
#
#  DRC_Csv2py.py INPUT_DRC.cvs OUTPUT_DRC.py
#
import sys
import csv
#
args  = sys.argv
#
ifile = args[1]
ofile = args[2]
hfile = "./DRC_csv2py.head"
#
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
def print_drc( f, row ) :
    #
    try : 
        float(row[2])
        print( "DR['%5s'] = DRule( %5.1f, '%s')" % (row[0], float(row[2]), row[1]), file=f )
    except :
        return

def print_head( ifile, ofile ) :
    #
    head = ifile.read()
    print('%s' % head, file=ofile )

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Main routine
#
head_file = open( hfile, "r", encoding="utf8")
csv_file  = open( ifile, "r", encoding="utf8")
py_file   = open( ofile, "w", encoding="utf8")
#
print_head( head_file, py_file )
#
csv = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

for row in csv:
    if row[0] != '' and row[0] != 'Name' :
        print_drc(py_file, row)

head_file.close()
csv_file.close()
py_file.close()

#close()
#
exit
