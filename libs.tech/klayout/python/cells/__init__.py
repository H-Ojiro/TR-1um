# TR-1um: Copyright 2025 OpenSUSI non-profit organaization 
#
# Original version was made by jun1okamura
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#
import pya
from .fet     import *
from .cont    import *

# It's a Python class that inherits from the pya.Library class
class tr_1um(pya.Library):

    def __init__(self):
        # Set the description
        self.description = "TR-1um Pcells library"

    # Create the PCell declarations
        # MOS DEVICES
        self.layout().register_pcell("pfet",  pfet())
        self.layout().register_pcell("nfet",  nfet())
        #
        self.layout().register_pcell("contp", cont_po())
        #
        # CAP Devices 
        #self.layout().register_pcell("cap",  cap()) # CSIO device
        # RES Devices 
        #self.layout().register_pcell("res_diff", cap()) # Diff resistance
        #self.layout().register_pcell("res_poly", cap()) # Poly resistance

        # Register us with the name "TR-1um".
        self.register("TR-1um")

