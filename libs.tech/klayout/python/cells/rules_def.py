# TR-1um: Copyright 2025 OpenSUSI non-profit organaization 
#
# Original version was made by jun1okamura
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#
class DRule():
    def __init__(self, value: float, note: str) -> None:
        self.value = value
        self.note  = note

    def value(self) :
        return self.value

    def note(self) :
        return self.note

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
class Design_Rule( DRule ):
    #
    def __init__(self) -> None:
        self._dict = {}

    def __setitem__(self, key, desc: DRule) :
        if not isinstance(key, str):
            raise Exception()
        #
        # Prohibit Overwrite
        #
        if key in self._dict :
            raise KeyError(f"Key '{key}' already exists. Overwriting is not allowed.")
        #        
        self._dict[key]  = desc

    def __getitem__(self, key) :
        if not isinstance(key, str):
            raise Exception()
        return self._dict[key]

    @property
    def value(self, key) :
        return self._dict[key].value
    
    @property
    def note(self, key) :
        return self._dict[key].note

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
DR = Design_Rule()
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#
DR['WN.1'] = DRule(  8.0,  "WN width min" )
DR['WN.2'] = DRule( 12.0,  "WN space min" )
# AA in N-Well            
DR['AP.1'] = DRule(  1.4,  "Width min in WN" )
DR['AP.2'] = DRule(  1.4,  "Space min in WN" )
DR['AP.3'] = DRule(  2.8,  "AP-DP min to WN" )
DR['AP.4'] = DRule(  7.0,  "Enc   min to WN" )
DR['AN.5'] = DRule(  1.4,  "Width min in WN" )
DR['AN.6'] = DRule(  1.4,  "Space min in WN" )
DR['AN.7'] = DRule(  1.4,  "Enc   min to WN" )
DR['AP.N'] = DRule(  2.8,  "AP-AN min in WN" )
DR['AP.W'] = DRule(  3.4,  "PMOS W min     " )
# AA in PSUB
DR['AN.1'] = DRule(  1.4,  "Width min in WP" )
DR['AN.2'] = DRule(  1.4,  "Space min in WP" )
DR['AN.3'] = DRule(  2.8,  "AN-DN min to WN" )
DR['AN.4'] = DRule( 10.0,  "Sep   min to WN" )
DR['AP.5'] = DRule(  1.4,  "Width min in WP" )
DR['AP.6'] = DRule(  1.4,  "Space min in WP" )
DR['AP.7'] = DRule(  5.0,  "Sep   min to WN" )
DR['AN.P'] = DRule(  2.8,  "AN-AP min in WP" )
DR['AN.W'] = DRule(  3.4,  "NMOS W min     " )
# CO 
DR['CO.1'] = DRule(  1.0,  "Width min      " )
DR['CO.2'] = DRule(  1.0,  "Space min      " )
DR['CO.W'] = DRule(  1.2,  "Width          " )
# CO on AA
DR['CO.P'] = DRule(  0.8,  "ENC min to AP  " )
DR['CO.N'] = DRule(  0.8,  "ENC min to AN  " )
DR['CO.D'] = DRule(  1.2,  "ENC min to AD  " )
DR['CO.G'] = DRule(  1.0,  "CO-PG min in AA" )
DR['CO.O'] = DRule(  0.8,  "ENC min to PO  " )
DR['CO.M'] = DRule(  0.8,  "ENC min to M1  " )
# PO to AA related
DR['PO.1'] = DRule(  1.0,  "Width min      " )
DR['PO.2'] = DRule(  1.2,  "Space min      " )
DR['PO.P'] = DRule(  0.4,  "PO-AP min      " )
DR['PO.N'] = DRule(  0.4,  "PO-AN min      " )
#DR['PC.P'] = DRule(  1.0,  "PO-CO min in AP" )
#DR['PC.N'] = DRule(  1.0,  "PO-CO min in AN" )
DR['PO.E'] = DRule(  1.2,  "Endcap min     " )
