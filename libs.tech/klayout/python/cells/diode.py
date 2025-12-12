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

class diode_p(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(diode_p, self).__init__()
        #
        self.param("nx", self.TypeInt,  "X-Num", default=1)
        self.param("ny", self.TypeInt,  "Y-Num", default=1)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "diode_p(X-Num" + ('%3d' % self.nx) + ",Y-Num" + ('%3d' % self.ny) + ")"
    
    def coerce_parameters_impl(self):
        # Check parameters
        if self.nx != 1 :
            self.nx = 1
        if self.ny != 1 :
            self.ny = 1

    def produce_impl(self):
        #
        draw_acont( self.cell, width = DR['CO.W'].value, xnum=self.nx, ynum=self.ny )
        draw_plate( self.cell, width = DR['CO.W'].value, xnum=self.nx, ynum=self.ny, layer=M1_layer, enc=DR['CO.M'].value )
        draw_plate( self.cell, width = DR['CO.W'].value, xnum=self.nx, ynum=self.ny, layer=AP_layer, enc=DR['CO.D'].value )
      
class diode_n(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(diode_n, self).__init__()
        #
        self.param("nx", self.TypeInt,  "X-Num", default=1)
        self.param("ny", self.TypeInt,  "Y-Num", default=1)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "diode_n(X-Num" + ('%3d' % self.nx) + ",Y-Num" + ('%3d' % self.ny) + ")"
    
    def coerce_parameters_impl(self):
        # Check parameters
        if self.nx != 1 :
            self.nx = 1
        if self.ny != 1 :
            self.ny = 1

    def produce_impl(self):
        #
        draw_acont( self.cell, width = DR['CO.W'].value, xnum=self.nx, ynum=self.ny )
        draw_plate( self.cell, width = DR['CO.W'].value, xnum=self.nx, ynum=self.ny, layer=M1_layer, enc=DR['CO.M'].value )
        draw_plate( self.cell, width = DR['CO.W'].value, xnum=self.nx, ynum=self.ny, layer=AN_layer, enc=DR['CO.D'].value )
    
