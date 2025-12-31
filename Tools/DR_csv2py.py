#! /usr/bin/env python3
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# TR-1um DRC v0.001 
# Original version was made by jun1okamura from TokaiRika's document 
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- 
#
# DR_csv2py.py ../libs.tech/klayout/python/cells/rules_def.py
#
import sys
import csv
#
args  = sys.argv
#
ifile = '../Document/TR-1um_Drawing_Layer_DR_Table.csv'
hfile = "./DR_csv2py.head"
#
if len(args) > 1 :
    ofile = args[1]
else : 
    ofile = None
#
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
def print_drc( f, row ) :
    #
    try : 
        min = float(row[4])
        if row[5] == '' :
            max = -1.0 
        else :
            max = float(row[5])
        #
        print( "DR['%5s'] = DRule( %5.1f, %5.1f, '%s','%s','%s' )" % (row[0], min, max, row[1], row[2], row[3]), file=f )
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
#
if ofile == None :
    py_file = sys.stdout
else :
    py_file  = open( ofile, "w", encoding="utf8")
#
print_head( head_file, py_file )
#
csv = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

for row in csv:
    if row[0] != '' and row[0] != 'Rule' :
        print_drc(py_file, row)

head_file.close()
csv_file.close()
py_file.close()

#close()
#
exit
