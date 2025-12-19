# TR-1um: Copyright 2025 OpenSUSI non-profit organaization 
#
# Original version was made by jun1okamura
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#
import pya
from .layers_def import *
from .rules_def  import *
from .util       import *

class res_p(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(res_p, self).__init__()
        #
        self.param("l", self.TypeDouble, "L", default=10.0, unit="um")
        self.param("w", self.TypeDouble, "W", default=2.0,  unit="um")

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "res_p(L=" + ('%3f' % self.l) + ",W=" + ('%3f' % self.w) + ")"
    
    def coerce_parameters_impl(self):
        # Check parameters
        if self.w < DR['PR.W1'].value :
            self.w = DR['PR.W1'].value
        if self.l < DR['PR.L3'].value :
            self.l = DR['PR.L3'].value

    def produce_impl(self):
        #
        draw_res( self.cell, l=self.l, w=self.w, layer=PR_layer)

class res_d(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(res_d, self).__init__()
        #
        self.param("l", self.TypeDouble, "L", default=10.0, unit="um")
        self.param("w", self.TypeDouble, "W", default=2.0,  unit="um")

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "res_d(L=" + ('%3f' % self.l) + ",W=" + ('%3f' % self.w) + ")"
    
    def coerce_parameters_impl(self):
        # Check parameters
        if self.w < DR['AR.W1'].value :
            self.w = DR['AR.W1'].value
        if self.l < DR['AR.L3'].value :
            self.l = DR['AR.L3'].value

    def produce_impl(self):
        #
        draw_res( self.cell, l=self.l, w=self.w, layer=AR_layer, )
        draw_rpo( self.cell, l=self.l, w=self.w, layer=PG_layer)

