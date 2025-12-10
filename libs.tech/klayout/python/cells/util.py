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

co_width    = Design_Rule['CO.1']
co_space    = Design_Rule['CO.2']
co_enc_diff = Design_Rule['CO.P']
po_end      = Design_Rule['PO.E']

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# How many contacts can place within len
#
def len_2_num ( len : float = 1.0 ):    
    #
    len   = len - 2 * co_enc_diff               
    num_e = math.floor( len              / (co_width + co_space)) 
    num_o = math.floor((len  - co_width) / (co_width + co_space))
    if num_e == num_o :
        return(num_e + 1)
    else :
        return(num_e)

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Insert number of contacts into cell
#
def draw_cont ( cell, num : int = 1, x_disp : float = 0 ):
    #
    sign     = 1
    co_pitch = (co_width + co_space)
    co_box   = pya.DBox(-co_width/2.0, -co_width/2.0,  co_width/2.0,  co_width/2.0)
    #
    if num > 0 :
        for n in range(num) :
            if num % 2 == 0 :   # even number of contacts
                n2 = math.floor(n / 2)
                y_disp = sign * (co_pitch * n2 + co_pitch / 2)
            else :              # odd number of contacts
                n2 = math.ceil(n / 2)
                y_disp = sign * co_pitch * n2
            #
            cell.shapes(CO_layer).insert(co_box).transform(pya.DTrans( x_disp, y_disp ))
            #
            sign = sign * -1
    #

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# 
#
def draw_gate ( cell, l, w , po_s : float = 1.0, num : int = 1 ):
    #
    sign      = 1
    po_pitch  = l + po_s
    po_length = w + 2 * po_end
    #
    po_path = pya.DPath([pya.DPoint(0, -po_length/2), pya.DPoint(0, po_length/2)], l)
    #
    if num > 0 :
        for n in range(num) :
            if num % 2 == 0 :   # even number of gates
                n2 = math.floor(n / 2)
                x_disp = sign * (po_pitch * n2 + po_pitch / 2)
            else :              # odd number of gates
                n2 = math.ceil(n / 2)
                x_disp = sign * po_pitch * n2
            #
            cell.shapes(PG_layer).insert(po_path).transform(pya.DTrans( x_disp, 0 ))
            #
            sign = sign * -1
