#! /usr/bin/env python3
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# TR-1um DRC v0.001 
# Original version was made by jun1okamura from TokaiRika's document 
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- 
#
#  ./DRC_csv2drc.py ../Document/Layer_Tables/TR-1um_Drawing_Layer_DR_Table.csv ../libs.tech/klayout/drc/run.drc
#
import sys
import csv
#
args  = sys.argv
#
ifile = args[1]

if len(args) > 2 :
    ofile = args[2]
else : 
    ofile = None
hfile = "./DRC_csv2drc.head"
#
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Translater
#
L = {
    'WN'          : 'WN',
    'WN(R)'       : 'WR',
    'WN(C)'       : 'WC',
    'WN(M)'       : 'WN - WC',
    'AP'          : 'AP',
    'AN'          : 'AN',
    'AN(C)'       : 'AN & WC',
    'AR'          : 'AR',
    'AR(T)'       : 'AR, projection, two_sides_allowed',
    'AR(S)'       : 'AR',
    'AC'          : 'AC',
    'AP+AR'       : 'AP + AR',
    'AP+AC'       : 'AP + AC',
    'AP+AN'       : 'AP + AN',
    'AA+PO+PR'    : 'AA + PO + PR',
    'AP+AN+AC+AR' : 'AA',
    'AP-PO'       : 'AP - PO',
    'AN-PO'       : 'AN - PO',
    'PMOS'        : 'AP & PO',
    'NMOS'        : 'AN & PO',
    'DP'          : 'DP',
    'DN'          : 'DN',
    'PO+PR'       : 'PO + PR',
    'PO'          : 'PO',
    'PO&AP'       : 'PO & AP',
    'PO&AN'       : 'PO & AN',
    'PO-AP'       : 'PO - AP',
    'PO-AN'       : 'PO - AN',
    'PR'          : 'PR',
    'PO(G)'       : 'PO & AM',
    'PO(AR)'      : 'PO & WR',
    'CO'          : 'CO',
    'CO(L)'       : 'CL',
    'CO(S)'       : 'CO - CL',
    'CO(C)'       : 'CO & AC',
    'CO(R)'       : 'CO & WR',
    'CO(RR)'      : 'CO & AR',
    'CL(RR)'      : 'CL & AR',
    'CO(D)'       : 'CO & AD',
    'M1'          : 'M1',
    'M1(C)'       : 'M1C',
    'M1(W)'       : 'M1W',
    'V1'          : 'V1',
    'M2'          : 'M2',
    'Endcap'      : 'Endcap',
    'Bevel'       : 'Bevel',
    'TieDown'     : 'TieDown',
    'RR'          : 'RR',
    'RS'          : 'RS',
    'RR(L)'       : 'AR  - RR',
    'RS(L)'       : 'PR  - RS',
    'RR(W)'       : 'ARW - RR',
    'RS(W)'       : 'RSW - RS',
    ''            : 'XXX',
    }

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# print
#
def print_Zn ( f, rule, func, L1, L2, L3, L4, min, max ) :
    match L1 :
        case 'WR' | 'WC' :
            print( "(%-7s).covering(%5s).output('%-5s:%2s not in %2s')" % (L1,L2,rule,L4,L3), file=f)
            return
        case 'CO' :
            print( "(%2s - ( %-12s )).output('%-5s:%2s not on %s')" % (L1, L2, rule, L3, L4), file=f)
            return
        case 'V1' :
            print( "(%2s - ( %-12s )).output('%-5s:%2s not on %s')" % (L1, L2, rule, L3, L4), file=f)
            return
    print(rule)

def print_Sn ( f, rule, func, L1, L2, L3, L4, min, max ) :
        if L1 == L2 :
            print( "(%-7s).drc(             space < %4.1f ).output('%-5s:%2s %s < %4.1f')" % (L1,min,rule,L3,func,min), file=f)
            return
        elif L1 == 'M1W' :
            print( "# ----- M1(Wide) -----", file=f)
            print( "(%-7s).drc(  sep(%2s, projection, projecting >= 10.0 ) < %4.1f).output('%-5s:%2s %s < %4.1f')" % (L1,L2,min,rule,L3,func,min), file=f)
            print( "# ", file=f)
            return
        else :
            print( "(%-7s).drc(      sep(%-7s) < %4.1f ).output('%-5s:%2s-%s %s < %4.1f')" % (L1,L2,min,rule,L3,L4,func,min), file=f)

def print_MX ( f, rule, func, L1, L2, L3, L4, min, max ) :
    match rule :
        case 'AC.W1' :
            print( "(%-7s).drc(           width <  %5.1f ).output('%-5s:%2s Wmin < %5.1f')" % (L1,min,rule,L3,min), file=f)
            print( "(%-7s).drc(           width >  %5.1f ).output('%-5s:%2s Wmax > %5.1f')" % (L1,max,rule,L3,max), file=f)
            return
        case 'PR.W1' | 'AR.W1' :
            print( "# ----- RES(W) -----", file=f)
            print( "(%-7s).sep((%-7s), 0.1, projection, projecting < %5.1f ).output('%-5s:%2s Wmin < %5.1f')" % (L1,L2,min,rule,L3,min), file=f)
            print( "(%-7s).sep((%-7s), 0.1, projection, projecting > %5.1f ).output('%-5s:%2s Wmax > %5.1f')" % (L1,L2,max,rule,L3,max), file=f)
            print( "# ", file=f)
            return
        case 'PR.L1' | 'AR.L1' :
            print( "# ----- RES(L) -----", file=f)
            print( "(%-7s).sep((%-7s), 0.1, projection, projecting < %5.1f ).output('%-5s:%2s Lmin < %5.1f')" % (L1,L2,min,rule,L3,min), file=f)
            print( "(%-7s).sep((%-7s), 0.1, projection, projecting > %5.1f ).output('%-5s:%2s Lmax > %5.1f')" % (L1,L2,max,rule,L3,max), file=f)
            print( "# ", file=f)
            return
        case 'AP.WM' | 'AN.WM' :
            print( "# ----- MOS(W) -----", file=f)
            print( "(%-7s).sep((%-7s), 0.1, projection, projecting < %5.1f ).output('%-5s:%2s Wmin < %5.1f')" % (L1,L2,min,rule,L3,min), file=f)
            print( "(%-7s).sep((%-7s), 0.1, projection, projecting > %5.1f ).output('%-5s:%2s Wmax > %5.1f')" % (L1,L2,max,rule,L3,max), file=f)
            print( "# ", file=f)
            return
        case 'AP.LM' | 'AN.LM' :
            print( "# ----- MOS(L) -----", file=f)
            print( "(%-7s).sep((%-7s), 0.1, projection, projecting < %5.1f ).output('%-5s:%2s Lmin < %5.1f')" % (L1,L2,min,rule,L3,min), file=f)
            print( "(%-7s).sep((%-7s), 0.1, projection, projecting > %5.1f ).output('%-5s:%2s Lmax > %5.1f')" % (L1,L2,max,rule,L3,max), file=f)
            print( "# ", file=f)
            return
    print(rule, func)

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# read_line
#
def gen_drc( f, rule, func, L1, L2, L3, L4, min, max ) :
    match func :
        case 'None' :
            print_Zn ( f, rule, func, L1, L2, L3, L4, min, max )
            return
        case 'Wmin' :
            print( "(%-7s).drc(             width < %4.1f ).output('%-5s:%2s %s < %4.1f')" % (L1,min,rule,L3,func,min), file=f)
            return
        case 'Wfix' :
            print( "(%-7s).drc(            width != %4.1f ).output('%-5s:%2s %s < %4.1f')" % (L1,min,rule,L3,func,min), file=f)
            return
        case 'Wmin/max' | 'Lmin/max' :
            print_MX ( f, rule, func, L1, L2, L3, L4, min, max )
            return
        case 'Smin' :
            print_Sn ( f, rule, func, L1, L2, L3, L4, min, max )
            return
        case 'Emin' :
            print( "(%-7s).drc( enclosed(%-7s) < %4.1f ).output('%-5s:%2s-%s %s < %4.1f')" % (L1,L2,min,rule,L3,L4,func,min), file=f) 
            return
        case 'Fmin' :
            print( "(%-7s).drc(enclosing(%-7s) < %4.1f ).output('%-5s:%2s-%s %s < %4.1f')" % (L1,L2,min,rule,L3,L4,func,min), file=f)
            return
        case 'ECmin' :
            print( "# ----- MOS(EndCap) -----", file=f)
            print( "(%-7s).drc( enclosed(%2s, projection, without_touching_edges ) < %4.1f).output('%-5s:%2s Endcap < %4.1f')" % (L1,L2,min,rule,L3,min), file=f) 
            print( "# ", file=f)
            return
        case 'Donut' :
            print( "# ----- Surrounded -----", file=f)
            print( "(%-2s - (%-7s).holes                   ).output('%-5s:%2s must surrounded %s')"            % (L1,L2,rule,L3, L4), file=f) 
            print( "# ", file=f)
            return
        case 'XYmin' :
            print( "# ----- AR beveling -----", file=f)
            print( "(%-7s).drc( primary.edges.count != 8 ).output('%-5s:%2s shape NOT Octagon')"          % (L1,rule,L3), file=f)   
            print( "(%-2s.extents - %2s).drc(       area < 0.5 ).output('%-5s:%2s trimed corner size < %4.1f')" % (L1,L1,rule,L3,min/2), file=f)   
            print( "# ", file=f)
            return
    print(rule, func)

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# read_line
#
def read_line( f, row ) :
    #
    if row[0] == '#' :
        print( "# ----- ----- ----- ----- ----- ----- ----- ----- ", file=f)
        print( "# NOTICE: THIS IS AUTO-GENERATED by DRC_csv2drc.py", file=f)
        print( "# NOTICE: DO NOT EDIT DIRECTLY", file=f)
        print( "# ----- ----- ----- ----- ----- ----- ----- ----- ", file=f)
        print( "# %-s" % row[1], file=f)
        print( "#", file=f)
    #
    elif row[0] == 'Rule' :
        return
    #
    elif row[4] == '???' :
        return
    #
    else :        
        rule = row[0].replace(' ', '')      # delete space
        L1   = L[row[1].replace(' ', '')]   # delete space  
        L2   = L[row[2].replace(' ', '')]   # delete space  
        L3   = row[1].replace(' ', '')          # delete space  
        L4   = row[2].replace(' ', '')          # delete space  
        func = row[3].replace(' ', '')      # delete space
        #
        min = float(row[4])
        if row[5] == '' :
            max = -1.0 
        else :
            max = float(row[5])
        gen_drc ( f, rule, func, L1, L2, L3, L4, min, max )
        # print( "ERR:", row )
        return

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Print head
#
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
    drc_file = sys.stdout
else :
    drc_file  = open( ofile, "w", encoding="utf8")
#
print_head( head_file, drc_file )
#
csv = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

for row in csv:
    if row[0] != '' :
        read_line( drc_file, row )

head_file.close()
csv_file.close()
drc_file.close()
#
exit
