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
        super(cont_p, self).__init__()
        #
        self.param("nx", self.TypeInt,  "X-Num", default=1)
        self.param("ny", self.TypeInt,  "Y-Num", default=1)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "pcont(X-Num" + ('%3d' % self.nx) + ",Y-Num" + ('%3d' % self.ny) + ")"
    
    def produce_impl(self):
        #
        draw_acont( self.cell, xnum=self.nx, ynum=self.ny )
        draw_poly ( self.cell, xnum=self.nx, ynum=self.ny )
      
class cont_v1(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(cont_p, self).__init__()
        #
        self.param("nx", self.TypeInt,  "X-Num", default=1)
        self.param("ny", self.TypeInt,  "Y-Num", default=1)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "pcont(X-Num" + ('%3d' % self.nx) + ",Y-Num" + ('%3d' % self.ny) + ")"
    
    def produce_impl(self):
        #
        draw_acont( self.cell, xnum=self.nx, ynum=self.ny )
        draw_poly ( self.cell, xnum=self.nx, ynum=self.ny )
      
