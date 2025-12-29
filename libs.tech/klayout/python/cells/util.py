# TR-1um: Copyright 2025 OpenSUSI non-profit organaization 
#
# Original version was made by jun1okamura
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#
import pya
import math
from .layers_def import *
from .rules_def  import *

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# How many contacts can place within len
#
def len_2_num ( len : float = 1.0, 
               co_w : float = DR['CO.W1'].min, 
               co_s : float = DR['CO.S1'].min, 
               co_e : float = DR['CO.AP'].min ):    
    #
    len   = len - 2 * co_e
    num_e = math.floor( len          / (co_w + co_s)) 
    num_o = math.floor((len  - co_w) / (co_w + co_s))
    if num_e == num_o :
        return(num_e + 1)
    else :
        return(num_e)

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert Metal on the contact
#
def draw_metal( cell,
                co_w   : float = DR['CO.W1'].min, 
                co_s   : float = DR['CO.S1'].min, 
                co_e   : float = DR['M1.CO'].min, 
                x_size : float = 0,
                y_size : float = 0,
                x_disp : float = 0, 
                y_disp : float = 0, 
                x_0    : str = 'c', 
                y_0    : str = 'c', 
                keep   : bool = True,
                layer = M1_layer ):
    #
    x_num = len_2_num ( x_size, co_w = co_w, co_s = co_s, co_e = co_e )
    y_num = len_2_num ( y_size, co_w = co_w, co_s = co_s, co_e = co_e )
    #
    co_p  = (co_w + co_s)
    #
    if keep == True :
        x_len = x_size / 2.0
        y_len = y_size / 2.0
    else :
        if x_num % 2 == 0 : # even number of contacts
            n2 = math.floor((x_num - 1)/ 2)
            x_len = (co_p * n2 + co_p / 2) + co_w / 2 + co_e
        else :              # odd number of contacts
            n2 = math.ceil((x_num - 1) / 2)
            x_len = co_p * n2 + co_w / 2 + co_e
        #
        if y_num % 2 == 0 : # even number of contacts
            n2 = math.floor((y_num - 1)/ 2)
            y_len = (co_p * n2 + co_p / 2) + co_w / 2 + co_e
        else :              # odd number of contacts
            n2 = math.ceil((y_num - 1) / 2)
            y_len = co_p * n2 + co_w / 2 + co_e
    #
    if x_0 == 'l' :     # X offset
        x_disp = x_disp - (x_size / 2 - x_len)
    elif x_0 == 'r' :
        x_disp = x_disp + (x_size / 2 - x_len)
    else :
        x_disp = x_disp 
    #
    if y_0 == 'b' :     # Y offset
        y_disp = y_disp - (y_size / 2 - y_len)
    elif y_0 == 't' :
        y_disp = y_disp + (y_size / 2 - y_len)
    else :
        y_disp = y_disp
    #
    box = pya.DBox(-x_len, -y_len, x_len, y_len) 
    #
    cell.shapes(layer).insert(box).transform(pya.DTrans( x_disp, y_disp ))
    #
  
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert Hole shape
#
def draw_hole ( cell, l, w, 
               thick : float = DR['AR.PW'].min, 
               sep   : float = DR['AR.PO'].min, 
               layer = PG_layer, 
               inlet = 0.0 ):
    #
    box_x  = l + 2 * ( thick + sep )
    box_y  = w + 2 * ( thick + sep )
    hole_x = l + 2 * ( sep )
    hole_y = w + 2 * ( sep )
    #
    if inlet > 0.0 :
        box   =  pya.DPolygon( [(-inlet/2.0,   -box_y/2.0 ), 
                                (-box_x/2.0,   -box_y/2.0 ),
                                (-box_x/2.0,    box_y/2.0 ),
                                ( box_x/2.0,    box_y/2.0 ),
                                ( box_x/2.0,   -box_y/2.0 ),
                                ( inlet/2.0,   -box_y/2.0 ),
                                ( inlet/2.0,   -hole_y/2.0),
                                ( hole_x/2.0,  -hole_y/2.0),
                                ( hole_x/2.0,   hole_y/2.0),
                                (-hole_x/2.0,   hole_y/2.0),
                                (-hole_x/2.0,  -hole_y/2.0),
                                (-inlet/2.0,   -hole_y/2.0) ] )
        cell.shapes(layer).insert(box)
    else :
        box   =  pya.DPolygon(  [(-box_x/2.0,  -box_y/2.0),
                                (-box_x/2.0,   box_y/2.0),
                                ( box_x/2.0,   box_y/2.0),
                                ( box_x/2.0,  -box_y/2.0) ] )
        hole  =  pya.DBox( -hole_x/2.0, -hole_y/2.0,  hole_x/2.0,  hole_y/2.0 )
        #                      
        cell.shapes(layer).insert(box.insert_hole(hole))
    #

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert long shape of contacts into cell
#
def draw_lcont ( cell, 
                x_size : float = DR['CO.W1'].min, 
                y_size : float = DR['CO.W1'].min, 
                x_disp : float = 0, 
                y_disp : float = 0, 
                layer = CO_layer ):
    #
    co_box   =  pya.DBox(-x_size/2.0, -y_size/2.0,  x_size/2.0,  y_size/2.0)
    #
    cell.shapes(layer).insert(co_box).transform(pya.DTrans( x_disp, y_disp ))
    #

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert number of contacts into cell
#
def draw_cont ( cell, 
                co_w   : float = DR['CO.W1'].min, 
                co_s   : float = DR['CO.S1'].min,
                co_e   : float = DR['CO.PO'].min,
                x_size : float = 0,
                y_size : float = 0,
                x_disp : float = 0, 
                y_disp : float = 0, 
                x_0    : str = 'c',
                y_0    : str = 'c',
                layer = CO_layer ):
    #
    x_num = len_2_num ( x_size, co_w = co_w, co_s = co_s, co_e = co_e )
    y_num = len_2_num ( y_size, co_w = co_w, co_s = co_s, co_e = co_e )
    #
    sign   = 1.0
    pitch  = (co_w + co_s)
    co_box = pya.DBox(-co_w/2.0, -co_w/2.0,  co_w/2.0,  co_w/2.0)
    #
    for n in range(y_num) :
        if y_0 == 'c' and y_num % 2 == 0 :  # even number of contacts
            n2 = math.floor(n / 2)
            disp = sign * (pitch * n2 + pitch / 2)
        elif y_0 == 'c' :                   # odd number of contacts
            n2 = math.ceil(n / 2)
            disp = sign * pitch * n2
        elif y_0 == 'b' :                   # start from south
            disp =  1.0 * pitch * n - (y_size / 2.0 - co_e - co_w / 2)
        elif y_0 == 't' :                   # start from north
            disp = -1.0 * pitch * n + (y_size / 2.0 - co_e - co_w / 2)
        #
        cell.shapes(layer).insert(co_box).transform(pya.DTrans( x_disp, disp ))
        #
        sign = sign * -1
    #
    for n in range(x_num) :
        if x_0 == 'c' and x_num % 2 == 0 :  # even number of contacts
            n2 = math.floor(n / 2)
            disp = sign * (pitch * n2 + pitch / 2)
        elif x_0 == 'c' :                   # odd number of contacts
            n2 = math.ceil(n / 2)
            disp = sign * pitch * n2
        elif x_0 == 'l' :                   # start from west
            disp =  1.0 * pitch * n - (x_size / 2.0 - co_e - co_w / 2)
        elif x_0 == 'r' :                   # start from east
            disp = -1.0 * pitch * n + (x_size / 2.0 - co_e - co_w / 2)
        #
        cell.shapes(layer).insert(co_box).transform(pya.DTrans( disp, y_disp ))
        #
        sign = sign * -1
    #

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert X-Y array of contacts into cell
#
def draw_acont ( cell, 
                co_w   : float = DR['CO.W1'].min, 
                co_s   : float = DR['CO.S1'].min,
                co_e   : float = DR['CO.PO'].min,
                x_size : float = 0,
                y_size : float = 0,
                x_disp : float = 0, 
                y_disp : float = 0, 
                x_0    : str = 'c',
                y_0    : str = 'c',
                layer = CO_layer ):
    #
    x_num = len_2_num ( x_size, co_w = co_w, co_s = co_s, co_e = co_e )
    #
    sign   = 1.0
    pitch  = (co_w + co_s)
    #
    for n in range(x_num) :
        if x_0 == 'c' and x_num % 2 == 0 :   # even number of contacts
            n2 = math.floor(n / 2)
            x_disp = sign * (pitch * n2 + pitch / 2)
        elif x_0 == 'c' :
            n2 = math.ceil(n / 2)
            x_disp = sign * pitch * n2
        elif x_0 == 'l' :                    # start from west
            x_disp =  1.0 * pitch * n - (x_size / 2.0 - (co_e + co_w / 2))
        elif x_0 == 'r' :                    # start from east
            x_disp = -1.0 * pitch * n + (x_size / 2.0 - (co_e + co_w / 2))
        #
        print(co_w, co_s, co_e, x_disp, x_size, y_size, x_num)
        #
        draw_cont ( cell, 
                   co_w   = co_w, 
                   co_s   = co_s, 
                   co_e   = co_e, 
                   y_size = y_size, 
                   x_disp = x_disp,
                   y_0    = y_0, 
                   layer = layer )
        #
        sign = sign * -1

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#  Draw FET
#
def draw_fet( cell, l, w, layer, 
              co_w   : float = DR['CO.W1'].min, 
              po_s   : float = DR['PO.S1'].min, 
              co_e   : float = DR['CO.AP'].min, 
              co_pg  : float = DR['CO.PG'].min, 
              e_cap  : float = DR['PO.EM'].min,
              y_0    : str = 'c',
              fnum = 1):
    #
    sign    = 1.0
    po_p    = l + po_s
    po_len  = w + 2 * e_cap
    sdg_w   = l + 2 * (co_pg + co_w + co_e)
    m1_w    = co_w + 2 * co_e
    #
    po_path = pya.DPath([pya.DPoint(0, -po_len/2), pya.DPoint(0, po_len/2)], l)
    #
    for n in range(fnum) :
        if fnum % 2 == 0 :   # even number of gates
            n2 = math.floor(n / 2)
            x_disp = sign * (po_p * n2 + po_p / 2)
        else :              # odd number of gates
            n2 = math.ceil(n / 2)
            x_disp = sign * po_p * n2
        #
        cell.shapes(PG_layer).insert(po_path).transform(pya.DTrans( x_disp, 0 ))
        #
        #
        sign = sign * -1
    #
    sdg_w     = sdg_w + po_p * (fnum - 1)           # Width of SDG region
    co_disp   = sdg_w / 2 - co_e - co_w / 2         # Center of Contact
    #
    sdg_box = pya.DBox(-sdg_w/2.0,  -w/2.0, sdg_w/2.0, w/2.0 )
    #
    cell.shapes(layer).insert(sdg_box)                          # Draw AA
    #
    # Add CO
    # 
    draw_cont( cell, y_size = w, x_disp = -co_disp, y_0 = y_0, layer = CO_layer )
    draw_cont( cell, y_size = w, x_disp =  co_disp, y_0 = y_0, layer = CO_layer )
    #
    # Add M1
    # 
    draw_metal( cell, x_size = m1_w, y_size = w, x_disp = -co_disp, y_0 = y_0, keep = False)
    draw_metal( cell, x_size = m1_w, y_size = w, x_disp =  co_disp, y_0 = y_0, keep = False)

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#  Draw Poly Resistor 
#
def draw_res_p( cell, l, w ,
               co_w : float = DR['CO.W1'].min, 
               co_e : float = DR['CO.PO'].min, 
               layer = PR_layer):
    #
    res_len = l + co_width + 2 * co_enc 
    #
    res_box = pya.DBox(-res_len/2.0, -w/2.0,  res_len/2.0, w/2.0 )
    #
    # Draw PR
    #
    cell.shapes(layer).insert(res_box)                         
    #
    # Add CO
    # 
    draw_cont( cell, y_num=len_2_num( w ), x_disp = -l/2 )
    draw_cont( cell, y_num=len_2_num( w ), x_disp =  l/2 )
    #
    # Add M1
    # 
    draw_metal ( cell, num=len_2_num( w ), x_disp= -l/2 )
    draw_metal ( cell, num=len_2_num( w ), x_disp=  l/2 )
    #

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#  Draw Diff Resistor 
#
def draw_res_d( cell, l, w ,
               co_width : float = DR['CO.W1'].min, 
               co_enc :float = DR['CR.AS'].min, 
               co_top :float = DR['CR.AT'].min, 
               res_xy = DR['AR.XY'].min,
               layer = AR_layer ):
    #
    res_len = l + 2 * (co_width + co_top)
    cont_l  = w - (co_width + 2 * co_enc)
    x_disp  = (l + co_width) / 2
    #
    # Octagon shape
    #
    res_oct = pya.DPolygon( [ (-(res_len/2.0         ), (w/2.0 - res_xy)),
                              (-(res_len/2.0 - res_xy), (w/2.0         )),
                              ( (res_len/2.0 - res_xy), (w/2.0         )),
                              ( (res_len/2.0         ), (w/2.0 - res_xy)),
                              ( (res_len/2.0         ),-(w/2.0 - res_xy)),
                              ( (res_len/2.0 - res_xy),-(w/2.0         )),
                              (-(res_len/2.0 - res_xy),-(w/2.0         )),
                              (-(res_len/2.0         ),-(w/2.0 - res_xy)) ])
    #
    # Draw AR
    #
    cell.shapes(layer).insert(res_oct)                         
    #
    # Add CO (variable)
    # 
    draw_lcont ( cell, y_size = cont_l, x_disp= -x_disp)
    draw_lcont ( cell, y_size = cont_l, x_disp=  x_disp)
    #
    # Add M1
    # 
    draw_metal ( cell, num=len_2_num( w ), x_disp= -x_disp )
    draw_metal ( cell, num=len_2_num( w ), x_disp=  x_disp )
    #
    # Add PO hole 
    # 
    draw_hole ( cell, res_len, w )
    #               

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#  Draw Capacito
#
def draw_cap( cell, l, w , 
              cc_width : float = DR['CC.W1'].min, 
              cc_space : float = DR['CC.S1'].min, 
              cc_enc   : float = DR['CC.AC'].min,
              co_width : float = DR['CO.W1'].min, 
              co_space : float = DR['CO.S1'].min, 
              co_enc   : float = DR['CC.AN'].min, 
              m1_enc   : float = DR['M1.CO'].min, 
              an_sep   : float = DR['AC.AN'].min,
              inlet    : float = DR['M1.SC'].min,
              layer = AC_layer ):
    #
    cc_nx  = len_2_num ( l, width = cc_width, space = cc_space, enc = cc_enc )
    cc_ny  = len_2_num ( w, width = cc_width, space = cc_space, enc = cc_enc )
    #
    an_w   = co_width + 2 * co_enc
    box_x  = l + 2 * ( an_sep )
    box_y  = w + 2 * ( an_sep + an_w )
    co_lx  = l + 2 * ( an_sep + co_enc) + co_width
    co_ly  = w + 2 * ( an_sep + co_enc) + co_width
    co_xi  = (box_x + inlet) / 2 
    #
    co_nx  = len_2_num ( box_x, width = co_width, space = co_space, enc = co_enc )
    co_ny  = len_2_num ( box_y, width = co_width, space = co_space, enc = co_enc )
    co_ni  = len_2_num ((box_x - inlet)/2.0, width = co_width, space = co_space, enc = co_enc )
    #
    # BOX shape
    #
    ac_box   =  pya.DBox(-l/2.0, -w/2.0,  l/2.0,  w/2.0)
    #
    # Draw AC
    #
    cell.shapes(layer).insert(ac_box)                         
    #
    # Add CO (variable)
    # 
    draw_acont( cell, width=cc_width, space=cc_space, 
               xnum=cc_nx, ynum=cc_ny, layer=CO_layer )
    draw_plate( cell, width=cc_space, space=cc_space,
               xnum=cc_nx, ynum=cc_ny, layer=M1_layer, enc=cc_enc )
    #
    # Add AN hole 
    # 
    draw_hole ( cell, l, w , thick= an_w, sep = an_sep, layer = AN_layer )
    draw_hole ( cell, l, w , thick= an_w, sep = an_sep, layer = M1_layer, inlet = inlet)
    #
    draw_cont( cell, y_num=co_ny, x_disp = -co_lx / 2.0 )
    draw_cont( cell, y_num=co_ny, x_disp =  co_lx / 2.0 )
    draw_cont( cell, x_num=co_nx, y_disp =  co_ly / 2.0 )
    draw_cont( cell, x_num=co_ni, x_disp =  co_xi / 2.0, y_disp =  -co_ly / 2.0 )
    draw_cont( cell, x_num=co_ni, x_disp = -co_xi / 2.0, y_disp =  -co_ly / 2.0 )
    #

