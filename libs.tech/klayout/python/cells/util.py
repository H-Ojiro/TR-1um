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
def len_2_num ( len : float = 1.0 ):    
    #
    len   = len - 2 * DR['CO.AP'].value               
    num_e = math.floor( len                       / (DR['CO.W1'].value + DR['CO.S1'].value)) 
    num_o = math.floor((len  - DR['CO.W1'].value) / (DR['CO.W1'].value + DR['CO.S1'].value))
    if num_e == num_o :
        return(num_e + 1)
    else :
        return(num_e)

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert Metal on the contact
#
def draw_metal ( cell, num : int = 1, x_disp : float = 0 ):
    #
    co_pitch = (DR['CO.W1'].value +     DR['CO.S1'].value)
    m1_width = (DR['CO.W1'].value + 2 * DR['CO.M1'].value)
    #
    if num % 2 == 0 :   # even number of contacts
        n2 = math.floor((num - 1)/ 2)
        y_disp = (co_pitch * n2 + co_pitch / 2) + DR['CO.W1'].value / 2 + DR['CO.M1'].value
    else :              # odd number of contacts
        n2 = math.ceil((num - 1) / 2)
        y_disp = co_pitch * n2 + DR['CO.W1'].value / 2 + DR['CO.M1'].value
    #
    m1_path = pya.DPath([pya.DPoint(0, -y_disp), pya.DPoint(0, y_disp)], m1_width)
    #
    cell.shapes(M1_layer).insert(m1_path).transform(pya.DTrans( x_disp, 0 ))
    #

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert number of contacts into cell
#
def draw_acont ( cell, xnum : int = 1, ynum : int = 1 ):
    #
    sign     = 1.0
    co_pitch = (DR['CO.W1'].value + DR['CO.S1'].value)
    co_box   = pya.DBox(-DR['CO.W1'].value/2.0, -DR['CO.W1'].value/2.0,  DR['CO.W1'].value/2.0,  DR['CO.W1'].value/2.0)
    #
    for n in range(xnum) :
        if xnum % 2 == 0 :   # even number of contacts
            n2 = math.floor(n / 2)
            x_disp = sign * (co_pitch * n2 + co_pitch / 2)
        else :              # odd number of contacts
            n2 = math.ceil(n / 2)
            x_disp = sign * co_pitch * n2
        #
        draw_cont( cell, num = ynum , x_disp = x_disp )
        #
        sign = sign * -1

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#  Draw Bottom/Top plate for contact
#
def draw_plate ( cell, width : float = DR['CO.W1'].value, space : float = DR['CO.S1'].value,
                xnum : int = 1, ynum : int = 1, layer = PG_layer, enc = 1.0 ):
    #
    pitch = (width + space)
    #
    if ynum % 2 == 0 :   # even number of contacts
        n2 = math.floor((ynum - 1)/ 2)
        y_disp = (pitch * n2 + pitch / 2) + width / 2
    else :              # odd number of contacts
        n2 = math.ceil((ynum - 1) / 2)
        y_disp =  pitch * n2 + width / 2 
    #
    if xnum % 2 == 0 :   # even number of contacts
        n2 = math.floor((xnum - 1)/ 2)
        x_disp = (pitch * n2 + pitch / 2) + width / 2
    else :              # odd number of contacts
        n2 = math.ceil((xnum - 1) / 2)
        x_disp =  pitch * n2 + width / 2 
    #
    box = pya.DBox(-(x_disp + enc),-(y_disp + enc), (x_disp + enc), (y_disp + enc))
    #                      
    cell.shapes(layer).insert(box)
    #

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert number of contacts into cell
#
def draw_cont ( cell, width : float = DR['CO.W1'].value, space : float = DR['CO.S1'].value,
               num : int = 1, x_disp : float = 0, layer = CO_layer ):
    #
    sign  = 1.0
    pitch = (width + space)
    box   =  pya.DBox(-width/2.0, -width/2.0,  width/2.0,  width/2.0)
    #
    for n in range(num) :
        if num % 2 == 0 :   # even number of contacts
            n2 = math.floor(n / 2)
            y_disp = sign * (pitch * n2 + pitch / 2)
        else :              # odd number of contacts
            n2 = math.ceil(n / 2)
            y_disp = sign * pitch * n2
        #
        cell.shapes(layer).insert(box).transform(pya.DTrans( x_disp, y_disp ))
        #
        sign = sign * -1
    #

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert long shape of contacts into cell
#
def draw_lcont ( cell, x_size : float = DR['CO.W1'].value, y_size : float = DR['CO.W1'].value, 
               x_disp : float = 0, y_disp : float = 0, layer = CO_layer ):
    #
    box   =  pya.DBox(-x_size/2.0, -y_size/2.0,  x_size/2.0,  y_size/2.0)
    cell.shapes(layer).insert(box).transform(pya.DTrans( x_disp, y_disp ))
    #

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert X-Y array of contacts into cell
#
def draw_acont ( cell, width : float = DR['CO.W1'].value, space : float = DR['CO.S1'].value,
                xnum : int = 1, ynum : int = 1, layer = CO_layer ):
    #
    sign  = 1.0
    pitch = (width + space)
    box   = pya.DBox(-width/2.0, -width/2.0,  width/2.0,  width/2.0)
    #
    for n in range(xnum) :
        if xnum % 2 == 0 :   # even number of contacts
            n2 = math.floor(n / 2)
            x_disp = sign * (pitch * n2 + pitch / 2)
        else :              # odd number of contacts
            n2 = math.ceil(n / 2)
            x_disp = sign * pitch * n2
        #
        draw_cont( cell, width = width, space = space, num = ynum, x_disp = x_disp, layer = layer)
        #
        sign = sign * -1

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#  Draw FET
#
def draw_fet( cell, l, w ,layer, fnum = 1):
    #
    sign      = 1.0
    po_pitch  = l + DR['PO.S1'].valuee
    po_length = w + 2 * DR['PO.EC'].value
    sdg_width = l + 2 * (DR['CO.AP'].value + DR['CO.W1'].value + DR['CO.PO'].value)
    #
    po_path = pya.DPath([pya.DPoint(0, -po_length/2), pya.DPoint(0, po_length/2)], l)
    #
    for n in range(fnum) :
        if fnum % 2 == 0 :   # even number of gates
            n2 = math.floor(n / 2)
            x_disp = sign * (po_pitch * n2 + po_pitch / 2)
        else :              # odd number of gates
            n2 = math.ceil(n / 2)
            x_disp = sign * po_pitch * n2
        #
        cell.shapes(PG_layer).insert(po_path).transform(pya.DTrans( x_disp, 0 ))
        #
        #
        sign = sign * -1
    #
    sdg_width = sdg_width + po_pitch * (fnum - 1)               # Width of SDG region
    co_disp   = sdg_width / 2 - DR['CO.AP'].value - DR['CO.W1'].value / 2      # Center of Contact
    #
    sdg_box = pya.DBox(-sdg_width/2.0,  -w/2.0, sdg_width/2.0, w/2.0 )
    #
    cell.shapes(layer).insert(sdg_box)                          # Draw AA
    #
    # Add CO
    # 
    draw_cont( cell, num=len_2_num( w ), x_disp = -co_disp )
    draw_cont( cell, num=len_2_num( w ), x_disp =  co_disp )
    #
    # Add M1
    # 
    draw_metal( cell, num=len_2_num( w ), x_disp = -co_disp )
    draw_metal( cell, num=len_2_num( w ), x_disp =  co_disp )

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#  Draw Resistor 
#
def draw_res( cell, l, w ,layer, var = True):
    #
    res_len = l + DR['CO.W1'].value + 2 * DR['CO.PR'].value
    #
    res_box = pya.DBox(-w/2.0,  -res_len/2.0, w/2.0, res_len/2.0 )
    mes_box = pya.DBox(-w/2.0,  -l/2.0, w/2.0, l/2.0 )
    #
    cont_l  = w - 2 * DR['CO.PR'].value
    #
    # Draw PR
    #
    cell.shapes(layer).insert(res_box)                         
    cell.shapes(ME_layer).insert(mes_box)                         
    #
    # Add CO
    # 
    draw_lcont( cell, x_size=cont_l, y_disp = -l/2 )
    draw_lcont( cell, x_size=cont_l, y_disp =  l/2 )
    #
    # Add M1
    # 
    metal_x = cont_l + 2 * DR['CO.M1'].value
    metal_y = DR['CO.W1'].value + 2 * DR['CO.M1'].value
    #
    draw_lcont( cell, x_size=metal_x, y_size=metal_y, y_disp = -l/2, layer=M1_layer )
    draw_lcont( cell, x_size=metal_x, y_size=metal_y, y_disp =  l/2, layer=M1_layer )

