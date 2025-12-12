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

class cont_po(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(cont_po, self).__init__()
        #
        self.param("nx", self.TypeInt,  "X-Num", default=1)
        self.param("ny", self.TypeInt,  "Y-Num", default=1)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "cont_po(X-Num" + ('%3d' % self.nx) + ",Y-Num" + ('%3d' % self.ny) + ")"
    
    def coerce_parameters_impl(self):
        # Check parameters
        if self.nx < 1 :
            self.nx = 1
        if self.ny < 1 :
            self.ny = 1

    def produce_impl(self):
        #
        draw_acont( self.cell, xnum=self.nx, ynum=self.ny )
        draw_plate( self.cell, xnum=self.nx, ynum=self.ny, layer=M1_layer, enc=DR['CO.M'].value )
        draw_plate( self.cell, xnum=self.nx, ynum=self.ny, layer=PG_layer, enc=DR['CO.O'].value )
      
class cont_p(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(cont_p, self).__init__()
        #
        self.param("nx", self.TypeInt,  "X-Num", default=1)
        self.param("ny", self.TypeInt,  "Y-Num", default=1)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "cont_p(X-Num" + ('%3d' % self.nx) + ",Y-Num" + ('%3d' % self.ny) + ")"
    
    def coerce_parameters_impl(self):
        # Check parameters
        if self.nx < 1 :
            self.nx = 1
        if self.ny < 1 :
            self.ny = 1

    def produce_impl(self):
        #
        draw_acont( self.cell, xnum=self.nx, ynum=self.ny )
        draw_plate( self.cell, xnum=self.nx, ynum=self.ny, layer=M1_layer, enc=DR['CO.M'].value )
        draw_plate( self.cell, xnum=self.nx, ynum=self.ny, layer=AP_layer, enc=DR['CO.P'].value )
      
class cont_n(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(cont_n, self).__init__()
        #
        self.param("nx", self.TypeInt,  "X-Num", default=1)
        self.param("ny", self.TypeInt,  "Y-Num", default=1)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "cont_n(X-Num" + ('%3d' % self.nx) + ",Y-Num" + ('%3d' % self.ny) + ")"

    def coerce_parameters_impl(self):
        # Check parameters
        if self.nx < 1 :
            self.nx = 1
        if self.ny < 1 :
            self.ny = 1

    def produce_impl(self):
        #
        draw_acont( self.cell, xnum=self.nx, ynum=self.ny )
        draw_plate( self.cell, xnum=self.nx, ynum=self.ny, layer=M1_layer, enc=DR['CO.M'].value )
        draw_plate( self.cell, xnum=self.nx, ynum=self.ny, layer=AN_layer, enc=DR['CO.N'].value )
    
