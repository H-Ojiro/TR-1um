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
DR['WN.W1'] = DRule(  8.0,  "WN width min" )
DR['WN.S2'] = DRule( 12.0,  "WN space min" )
# AA in N-Well            
DR['AP.W1'] = DRule(  1.4,  "Width min in WN" )
DR['AP.S2'] = DRule(  1.4,  "Space min in WN" )
DR['AP.DP'] = DRule(  2.8,  "AP-DP min to WN" )
DR['AP.WN'] = DRule(  7.0,  "Enc   min to WN" )
DR['AN.W5'] = DRule(  1.4,  "Width min in WN" )
DR['AN.S6'] = DRule(  1.4,  "Space min in WN" )
DR['AN.E7'] = DRule(  1.4,  "Enc   min to WN" )
DR['AP.AN'] = DRule(  2.8,  "AP-AN min in WN" )
DR['AP.MW'] = DRule(  3.4,  "PMOS W min     " )
# AA in PSUB
DR['AN.W1'] = DRule(  1.4,  "Width min in WP" )
DR['AN.S2'] = DRule(  1.4,  "Space min in WP" )
DR['AN.DP'] = DRule(  2.8,  "AN-DN min to WN" )
DR['AN.WN'] = DRule( 10.0,  "Sep   min to WN" )
DR['AP.W5'] = DRule(  1.4,  "Width min in WP" )
DR['AP.S6'] = DRule(  1.4,  "Space min in WP" )
DR['AP.S7'] = DRule(  5.0,  "Sep   min to WN" )
DR['AN.AP'] = DRule(  2.8,  "AN-AP min in WP" )
DR['AN.MW'] = DRule(  3.4,  "NMOS W min     " )
# AR 
DR['AR.W1'] = DRule(  2.6,  "AR Width min   " )
DR['AR.S2'] = DRule(  2.0,  "AR Space min   " )
DR['AR.L3'] = DRule(  4.0,  "AR Length min  " )
# CO 
DR['CO.W1'] = DRule(  1.0,  "Width min      " )
DR['CO.S2'] = DRule(  1.0,  "Space min      " )
DR['CO.WS'] = DRule(  1.2,  "Width size     " )
# CO on AA
DR['CO.AP'] = DRule(  0.8,  "ENC min to AP  " )
DR['CO.AN'] = DRule(  0.8,  "ENC min to AN  " )
DR['CO.AD'] = DRule(  1.2,  "ENC min to AD  " )
DR['CO.PO'] = DRule(  1.0,  "CO-PO min in AA" )
## RES
DR['CO.PG'] = DRule(  0.8,  "ENC min to PG  " )
DR['CO.PR'] = DRule(  0.8,  "ENC min to PR  " )
DR['CO.AR'] = DRule(  0.8,  "ENC min to AR  " )
DR['CO.AT'] = DRule(  1.5,  "ENC min to ART " )
DR['CO.M1'] = DRule(  0.8,  "ENC min to M1  " )
# PO to AA related
DR['PO.W1'] = DRule(  1.0,  "Width min      " )
DR['PO.S2'] = DRule(  1.2,  "Space min      " )
DR['PO.AP'] = DRule(  0.4,  "PO-AP min      " )
DR['PO.AN'] = DRule(  0.4,  "PO-AN min      " )
#DR['PC.P'] = DRule(  1.0,  "PO-CO min in AP" )
#DR['PC.N'] = DRule(  1.0,  "PO-CO min in AN" )
DR['PO.EC'] = DRule(  1.2,  "Endcap min     " )
# PR 
DR['PR.W1'] = DRule(  2.6,  "PR Width min   " )
DR['PR.S2'] = DRule(  2.0,  "PR Space min   " )
DR['PR.L3'] = DRule(  4.0,  "PR Length min  " )
# CO 
# V1 
DR['V1.W1'] = DRule(  1.4,  "Width min      " )
DR['V1.S2'] = DRule(  1.5,  "Space min      " )
# CO on AA
DR['V1.M1']= DRule(  1.0,  "ENC min to M1  " )
DR['V1.M2']= DRule(  1.0,  "ENC min to M2  " )
