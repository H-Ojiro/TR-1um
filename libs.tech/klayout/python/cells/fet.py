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

class pfet(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(pfet, self).__init__()
        #
        self.param("type", self.TypeString, "Type", default="PFET")
        #
        self.param("l", self.TypeDouble, "Length",  default=DR['PO.1'].value, unit="um")
        self.param("w", self.TypeDouble, "Width",   default=DR['AP.W'].value, unit="um")
        self.param("n", self.TypeInt,    "Fingers", default=1)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "pfet(L=" + ('%.3f' % self.l) + ",W=" + ('%.3f' % self.w) + ")"
    
    '''
    def coerce_parameters_impl(self):
        self.a = self.w * self.l

    def can_create_from_shape_impl(self):
        # OPTIONAL: Implement the "Create PCell from shape" protocol: we can use any shape which
        # has a finite bounding box
        print("Shape:" + self.shape.is_box() or self.shape.is_polygon() or self.shape.is_path())
        return self.shape.is_box() or self.shape.is_polygon() or self.shape.is_path()

    def parameters_from_shape_impl(self):
        # OPTIONAL: Implement the "Create PCell from shape" protocol:
        # bounding box width and layer
        print(self.layout.get_info(self.layer))
        self.b = self.shape.bbox().width() * self.shape.bbox().height()
    
    def transformation_from_shape_impl(self):
        # OPTIONAL: Implement the "Create PCell from shape" protocol: we use the center of the shape's
        # bounding box to determine the transformation
        return pya.Trans(self.shape.bbox().center())
    '''   
  
    def produce_impl(self):
        #
        draw_fet( self.cell, l=self.l, w=self.w, fnum=self.n, layer=AP_layer)
        #
      
class nfet(pya.PCellDeclarationHelper):

    def __init__(self):
        # Initialize super class.
        super(nfet, self).__init__()
        #
        self.param("type", self.TypeString, "Type", default="NFET")
        #
        self.param("l", self.TypeDouble, "Length",  default=DR['PO.1'].value, unit="um")
        self.param("w", self.TypeDouble, "Width",   default=DR['AN.W'].value, unit="um")
        self.param("n", self.TypeInt,    "Fingers", default=1)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "nfet(L=" + ('%.3f' % self.l) + ",W=" + ('%.3f' % self.w) + ")"
 
    def produce_impl(self):
        #
        draw_fet( self.cell, l=self.l, w=self.w, fnum=self.n, layer=AN_layer)
        #       
