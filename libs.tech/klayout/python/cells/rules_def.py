# TR-1um: Copyright 2025 OpenSUSI non-profit organaization 
#
# Original version was made by jun1okamura
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#
Design_Rule = {
    # N-Well
    'WN.1'  :  8.0,     # WN width min
    'WN.2'  : 12.0,     # WN space min
    # AA in N-Well            
    'AP.1'  :  1.4,     # Width min in WN
    'AP.2'  :  1.4,     # Space min in WN
    'AP.3'  :  2.8,     # AP-DP min to WN
    'AP.4'  :  7.0,     # Enc   min to WN
    'AN.5'  :  1.4,     # Width min in WN
    'AN.6'  :  1.4,     # Space min in WN
    'AN.7'  :  1.4,     # Enc   min to WN
    'AP.N'  :  2.8,     # AP-AN min in WN
    'AP.W'  :  3.4,     # PMOS W min     
    # AA in PSUB
    'AN.1'  :  1.4,     # Width min in WP
    'AN.2'  :  1.4,     # Space min in WP
    'AN.3'  :  2.8,     # AN-DN min to WN
    'AN.4'  : 10.0,     # Sep   min to WN
    'AP.5'  :  1.4,     # Width min in WP
    'AP.6'  :  1.4,     # Space min in WP
    'AP.7'  :  5.0,     # Sep   min to WN
    'AN.P'  :  2.8,     # AN-AP min in WP
    'AN.W'  :  3.4,     # NMOS W min     
    # CO 
    'CO.1'  :  1.0,     # Width min      
    'CO.2'  :  1.0,     # Space min      
    'CO.W'  :  1.2,     # Width          
    # CO on AA
    'CO.P'  :  0.8,     # ENC min to AP  
    'CO.N'  :  0.8,     # ENC min to AN  
    'CO.D'  :  1.2,     # ENC min to AD  
    'CO.O'  :  0.8,     # ENC min to PO  
    # PO to AA related
    'PO.1'  :  1.0,     # Width min      
    'PO.2'  :  1.2,     # Space min      
    'PO.P'  :  0.4,     # PO-AP min      
    'PO.N'  :  0.4,     # PO-AN min      
    'PC.P'  :  1.0,     # PO-CO min in AP
    'PC.N'  :  1.0,     # PO-CO min in AN
    'PO.E'  :  1.2,     # Endcap min     
}









