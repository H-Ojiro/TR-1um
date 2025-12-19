#! /usr/bin/env python3
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# TR-1um DRC v0.001 
# Original version was made by jun1okamura from TokaiRika's document 
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- 
#
#  IP62_to_TR-1um.py INPUT_IP62_GDS OUTPUT_TR-1um_GDS 
#
import sys
import klayout.db as db
#
ly    = db.Layout()  
args  = sys.argv
#
ifile = args[1]
ofile = args[2]
#
ly.read(ifile)
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# IP62
PSUB = ly.layer(140, 0)     
NW   = ly.layer( 36, 0)     
HVNW = ly.layer(141, 0)     
L    = ly.layer(  3, 0)     
NF   = ly.layer( 25, 0)     # L1
PF   = ly.layer( 26, 0)     # L2
HPBE = ly.layer(144, 0)     # L3
HNBE = ly.layer(145, 0)     # L4
PBE  = ly.layer(146, 0)     # L3
NBE  = ly.layer(147, 0)     # L4
SG   = ly.layer(  8, 0)     
PM   = ly.layer( 35, 0)     # L5
NM   = ly.layer(  7, 0)     # L6
PSD  = ly.layer(  9, 0)     # L7
NSD  = ly.layer( 28, 0)     # L8
R    = ly.layer( 12, 0)     # L9
CL   = ly.layer(143, 0)     # LA
HPM  = ly.layer( 33, 0)     
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# DLXXX 
DPBG  = ly.layer(116, 0)
DNBG  = ly.layer(117, 0)
DRBG  = ly.layer(118, 0)
DCBG  = ly.layer(119, 0)
DLWLMP= ly.layer(150, 0)
DLWLMN= ly.layer(151, 0)
DLWLRR= ly.layer(154, 0)
DLMP  = ly.layer(157, 0)
DLMN  = ly.layer(158, 0)
DLRR  = ly.layer(162, 0)
DLRS  = ly.layer(165, 0)
DLCSIO= ly.layer(166, 0)
DLDP  = ly.layer(167, 0)
DLDN  = ly.layer(168, 0)
DLMPE = ly.layer(169, 0)
DLMNE = ly.layer(170, 0)
DLBGMP= ly.layer(177, 0)
DLBGMN= ly.layer(178, 0)
DLBGRR= ly.layer(182, 0)
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Drawing Layers
#
AP    = ly.layer(  3, 1)
AN    = ly.layer(  3, 2)
AR    = ly.layer(  3, 3)
AC    = ly.layer(  3, 4)
#
PG    = ly.layer(  8, 1)
PR    = ly.layer(  8, 2)
#
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
def convert_drawing( cell : db.Cell ) :
    #
    NWCS = (db.Region(cell.shapes(PSUB)).merged() & 
            db.Region(cell.shapes(NW  )).merged().interacting(db.Region(cell.shapes(CL)).merged()))
    NWMP = (db.Region(cell.shapes(PSUB)).merged() & 
            db.Region(cell.shapes(NW  )).merged()).not_interacting(db.Region(cell.shapes(CL)).merged())
    NWRR = (db.Region(cell.shapes(PSUB)).merged() & db.Region(cell.shapes(HVNW)).merged())
    PWMN = (db.Region(cell.bbox()) - db.Region(cell.shapes(PSUB)).merged())
    #
    LG   = (db.Region(cell.shapes(L  )).merged()).interacting(db.Region(cell.shapes(SG)).merged())
    LX   = (db.Region(cell.shapes(L  )).merged()).not_interacting(db.Region(cell.shapes(SG)).merged())
    # 
    P1   = (db.Region(cell.shapes(SG )).merged() - db.Region(cell.shapes(DLRS)).merged())
    P2   = (db.Region(cell.shapes(SG )).merged() & db.Region(cell.shapes(DLRS)).merged())
    #
    L1   = (db.Region(cell.shapes(NF )).merged())
    L2   = (db.Region(cell.shapes(PF )).merged())
    L3   = (db.Region(cell.shapes(NBE)).merged())
    L4   = (db.Region(cell.shapes(PBE)).merged())
    L5   = (db.Region(cell.shapes(PM )).merged())
    L6   = (db.Region(cell.shapes(NM )).merged())
    L7   = (db.Region(cell.shapes(PSD)).merged())
    L8   = (db.Region(cell.shapes(NSD)).merged())
    L9   = (db.Region(cell.shapes(R  )).merged())
    LA   = (db.Region(cell.shapes(CL )).merged())
    #
    D1   = (db.Region(cell.shapes(DLMP  )).merged())
    D2   = (db.Region(cell.shapes(DLMN  )).merged())
    D3   = (db.Region(cell.shapes(DLMPE )).merged())
    D4   = (db.Region(cell.shapes(DLMNE )).merged())
    D5   = (db.Region(cell.shapes(DLDP  )).merged())
    D6   = (db.Region(cell.shapes(DLDN  )).merged())
    D7   = (db.Region(cell.shapes(DLBGMP)).merged())
    D8   = (db.Region(cell.shapes(DLBGMN)).merged())
    D9   = (db.Region(cell.shapes(DLRR  )).merged())
    DA   = (db.Region(cell.shapes(DLBGRR)).merged())
    DB   = (db.Region(cell.shapes(DLCSIO)).merged())
    #
    AAMP = (LG & ( NWMP & L1 & L2 - L3 & L4 - L5 & L6 - L7 & L8 - L9 - LA)) #| (LG & D1 )
    AAMN = (LG & ( PWMN - L1 - L2 & L3 - L4 & L5 - L6 & L7 - L8 - L9 - LA)) #| (LG & D2 )
    AAPE = (LG & ( NWMP & L1 & L2 - L3 & L4 - L5 & L6 - L7 & L8 - L9 - LA)) #| (LG & D3 )
    AANE = (LG & ( PWMN - L1 - L2 & L3 - L4 & L5 & L6 & L7 - L8 - L9 - LA)) #| (LG & D4 )
    #
    AADP = (LX & ( NWMP & L1 & L2 - L3 - L4 & L5 & L6 - L7 & L8 - L9 - LA)) #| (LX & D5 )  
    AADN = (LX & ( PWMN - L1 - L2 - L3 - L4 & L5 & L6 & L7 - L8 - L9 - LA)) #| (LX & D6 )  
    AAGP = (LX & ( NWMP & L1 & L2 - L3 - L4 & L5 & L6 & L7 - L8 - L9 - LA)) #| (LX & D7 )
    AAGN = (LX & ( PWMN - L1 - L2 - L3 - L4 & L5 & L6 - L7 & L8 - L9 - LA)) #| (LX & D8 )
    AARR = (LX & ( NWRR & L1 - L2 - L3 - L4 & L5 & L6      & L8 & L9 - LA)) | (LX & D9 )    
    AAGR = (LX & ( NWRR & L1 - L2 - L3 - L4 & L5 & L6 & L7 - L8 - L9 - LA)) | (LX & DA )
    AACC = (LG & ( NWCS & L1 - L2 - L3 - L4 & L5 & L6 & L7 & L8 - L9 & LA)) | (LG & NWCS & DB )
    AAGC = (LX & ( NWCS & L1 - L2 - L3 - L4 & L5 & L6 & L7 - L8 - L9 - LA)) | (LX & NWCS & D8 )
    # ----- ----- ----- -----  
    # Create Drawing
    # 
    for shape in (AAMP + AAPE + AAGN + AADP) :
       cell.shapes(AP).insert(db.Polygon(shape))
    #
    for shape in (AAMN + AANE + AAGP + AADN + AAGR + AAGC) :
       cell.shapes(AN).insert(db.Polygon(shape))
    #                
    for shape in (AARR) :
       cell.shapes(AR).insert(db.Polygon(shape))
    #                
    for shape in (AACC) :
       cell.shapes(AC).insert(db.Polygon(shape))
    #
    for shape in (P1) :
       cell.shapes(PG).insert(db.Polygon(shape))
    #
    for shape in (P2) :
       cell.shapes(PR).insert(db.Polygon(shape))
    #
    # ----- ----- ----- -----  
    # Delete IMPLANT Layers
    #
    for layer in ( NW, HVNW, L, NF, PF, HPBE, HNBE, PBE, NBE, PM, NM, SG, PSD, NSD, R, CL, HPM ) :
        cell.shapes(layer).clear()
    #
    # ----- ----- ----- -----  
    # Delete DLXXX Layers
    #
    for layer in ( DPBG, DNBG, DRBG, DCBG, DLWLMP, DLWLMN, DLWLRR, DLMP, DLMN,
                    DLRR, DLRS, DLCSIO, DLDP, DLDN, DLMPE, DLMNE, DLBGMP, DLBGMN, DLBGRR ) :
        cell.shapes(layer).clear()
    #

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Main routine
#
if ly.top_cells() != None :
    for idx in ly.each_cell_bottom_up() :
        cl = ly.cell(idx)
        cell_name = cl.name.split('_')
        #
        # Exclude Seal-Ring to delete IP62 Layers
        #
        if len(cell_name) > 3 :
            if (cell_name[0] == "chip") & (cell_name[1] == "outline") & (cell_name[2] == "462") :
                print("CELL(%2d):%-10s" % (idx, cl.name))
        else :
            convert_drawing(cl)
    #    
#           
ly.write(ofile)
#
exit
