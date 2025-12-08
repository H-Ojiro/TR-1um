# TR-1um: Copyright 2025 OpenSUSI non-profit organaization 
#
# Original version was made by jun1okamura
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#
import pya
from .layers_def import *

fet_lp   = 1.0
fet_wp   = 2.6

class pfet(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(pfet, self).__init__()
        #
        self.param("type", self.TypeString, "PFET")
        #
        self.param("l", self.TypeDouble, "Length", default=fet_lp, unit="um")
        self.param("w", self.TypeDouble, "Width",  default=fet_wp, unit="um")
        #

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "pfet(L=" + ('%.3f' % self.l) + ",W=" + ('%.3f' % self.w) + ")"
    
    '''
    def coerce_parameters_impl(self):
        return()

    def can_create_from_shape_impl(self):
        return self.shape.is_box() or self.shape.is_polygon() or self.shape.is_path()

    def parameters_from_shape_impl(self):
        self.r = self.shape.bbox().width() * self.layout.dbu / 2
        # self.l = self.layout.get_info(self.layer)
    
    def transformation_from_shape_impl(self):
        return pya.Trans(self.shape.bbox().center())
    '''
        
    def produce_impl(self):
        end_cap = 1.2       # end cap
        co2g_sp = 1.0       # contact to poly space
        co_w    = 1.0       # contact size
        co_enc  = 0.8       # contact enclosure
        #
        sdg_w   = self.l + 2 * (co2g_sp + co_w + co_enc)
        co_disp = self.l/2.0 + co2g_sp + co_w/2.0
        po_disp = self.w/2.0 + end_cap
        po_path = pya.DPath([pya.DPoint(0, -po_disp), pya.DPoint(0, po_disp)], self.l)
        sdg_box = pya.DBox(-sdg_w/2.0,  -self.w/2.0, sdg_w/2.0, self.w/2.0 )
        co_box  = pya.DBox(-co_w/2.0,   -co_w/2.0,   co_w/2.0,  co_w/2.0)
        #
        self.cell.shapes(PG_layer).insert(po_path)
        self.cell.shapes(AP_layer).insert(sdg_box)
        self.cell.shapes(CO_layer).insert(co_box).transform(pya.DTrans(-co_disp, 0))
        self.cell.shapes(CO_layer).insert(co_box).transform(pya.DTrans( co_disp, 0))
    #
      
