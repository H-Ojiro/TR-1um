#
# TR-1um: Copyright 2025 OpenSUSI non-profit organaization 
#
# Original version was made by jun1okamura
# LICENSE: Apache License Version 2.0, January 2004,
#          http://www.apache.org/licenses/
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
#
class DRule():
    def __init__(self, min: float, max: float, note: str) -> None:
        self.min  = min
        self.max  = max      
        self.note = note

    def min(self) :
        return self.min

    def max(self) :
        return self.max

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
    def min(self, key) :
        return self._dict[key].min
    
    @property
    def max(self, key) :
        return self._dict[key].max
    
    @property
    def note(self, key) :
        return self._dict[key].note

# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
DR = Design_Rule()
# ----- ------ ----- ----- ------ ----- ----- ------ ----- 

DR['WN.W1'] = DRule(   8.0,  -1.0, 'WN Wmin')
DR['WN.S1'] = DRule(  12.0,  -1.0, 'WN-WN Smin')
DR['WN.S2'] = DRule(   9.5,  -1.0, 'WN-WN(R) Smin')
DR['WN.S3'] = DRule(  12.0,  -1.0, 'WN-WN(C) Smin ')
DR['WN.S4'] = DRule(   9.5,  -1.0, 'WN(R)-WN(C) Smin ')
DR['WN.S5'] = DRule(   8.0,  -1.0, 'WN(R)-WN(R) Smin ')
DR['WN.S6'] = DRule(  12.0,  -1.0, 'WN(C)-WN(C) Smin ')
DR['WN.AP'] = DRule(  10.0,  -1.0, 'WN-AP Smin')
DR['WN.AN'] = DRule(   5.0,  -1.0, 'WN-AN Smin')
DR['AR.W1'] = DRule(   2.8,  20.0, 'AR Wmin/max')
DR['AR.S1'] = DRule(   4.0,  -1.0, 'AR Smin')
DR['AR.XY'] = DRule(   1.0,  -1.0, 'AR corner cut')
DR['AR.WR'] = DRule(  10.0,  -1.0, 'AR-WN(R) Emin')
DR['AN.WR'] = DRule(   5.0,  -1.0, 'AN-WN(R) Emin')
DR['AR.AN'] = DRule(   4.0,  -1.0, 'AR-AN Smin')
DR['AC.W1'] = DRule(  28.5, 120.0, 'AC Wmin/max')
DR['AN.WC'] = DRule(   3.0,  -1.0, 'AN-WN(C) Emin')
DR['AC.AN'] = DRule(   2.8,  -1.0, 'AC-AN Smin')
DR['AP.W1'] = DRule(   1.4,  -1.0, 'AP Wmin')
DR['AP.S1'] = DRule(   1.4,  -1.0, 'AP Smin')
DR['AP.AN'] = DRule(   2.8,  -1.0, 'AP-AN Smin')
DR['AP.WM'] = DRule(   3.4,  60.0, 'PMOS Wmin/max')
DR['AP.LM'] = DRule(   1.0,  30.0, 'PMOS Lmin/max')
DR['AP.WN'] = DRule(   7.0,  -1.0, 'AP-WN Emin')
DR['DP.W1'] = DRule(   1.4,  -1.0, 'AP Wmin')
DR['DP.AP'] = DRule(   2.8,  -1.0, 'DP-AP Smin')
DR['DP.AN'] = DRule(   2.8,  -1.0, 'DP-AN Smin')
DR['AN.W1'] = DRule(   1.4,  -1.0, 'AN Wmin')
DR['AN.S1'] = DRule(   1.4,  -1.0, 'AN Smin')
DR['AN.AP'] = DRule(   2.8,  -1.0, 'AN-AP Smin')
DR['AN.WM'] = DRule(   3.4,  60.0, 'NMOS Wmin')
DR['AN.LM'] = DRule(   1.0,  30.0, 'NMOS Lmin/max')
DR['AN.WN'] = DRule(   5.0,  -1.0, 'AN-WN Emin')
DR['DN.AP'] = DRule(   2.8,  -1.0, 'DP-AP Smin')
DR['DN.AN'] = DRule(   2.8,  -1.0, 'DP-AN Smin')
DR['PO.W1'] = DRule(   1.0,  30.0, 'PO Wmin')
DR['PO.S1'] = DRule(   1.2,  -1.0, 'PO Smin')
DR['PO.AP'] = DRule(   0.4,  -1.0, 'PO-AP Smin')
DR['PO.AN'] = DRule(   0.4,  -1.0, 'PO-AN Smin')
DR['PO.EM'] = DRule(   1.2,  -1.0, 'MOS Endcap min')
DR['CO.W1'] = DRule(   1.0,  -1.0, 'CO Wmin')
DR['CO.S1'] = DRule(   1.0,  -1.0, 'CO Smin')
DR['CO.WD'] = DRule(   1.2,  -1.0, 'CO(D) Width')
DR['CO.AP'] = DRule(   0.8,  -1.0, 'CO-AP Emin')
DR['CO.AN'] = DRule(   0.8,  -1.0, 'CO-AN Emin')
DR['CO.PG'] = DRule(   1.0,  -1.0, 'CO-PO(G) Smin')
DR['CO.PO'] = DRule(   0.8,  -1.0, 'CO-PO Emin')
DR['CO.AD'] = DRule(   1.2,  -1.0, 'CO-AD Emin')
DR['AR.L1'] = DRule(  13.0, 100.0, 'AR Lmin/max')
DR['AR.PO'] = DRule(   1.0,  -1.0, 'PO-AR Smin')
DR['AR.PW'] = DRule(   2.0,  -1.0, 'PO(AR) Wmin')
DR['PO.L1'] = DRule(  20.0, 200.0, 'PO(AR) Lmin/max ')
DR['PR.W1'] = DRule(   4.0,  20.0, 'PO(R) Wmin/max')
DR['PR.L1'] = DRule(  20.0, 100.0, 'PO(R) Lmin/max')
DR['PR.S1'] = DRule(   2.0,  -1.0, 'PO(R) Smin')
DR['CR.W1'] = DRule(   1.0,  -1.0, 'CO(RR) Width')
DR['CR.W2'] = DRule(   1.0,  -1.0, 'CO(RR) Wmin')
DR['CR.AT'] = DRule(   1.5,  -1.0, 'CO(RR)-AR(Top) Emin')
DR['CR.AS'] = DRule(   1.0,  -1.0, 'CO(RR)-AR(Side) Emin')
DR['CC.W1'] = DRule(   1.2,  -1.0, 'CO(C) Wmin')
DR['CC.S1'] = DRule(   1.2,  -1.0, 'CO(C) Smin')
DR['CC.AC'] = DRule(   2.9,  -1.0, 'CO(C)-AC Emin')
DR['CC.AN'] = DRule(   1.2,  -1.0, 'CO(C)-AN Emim')
DR['M1.W1'] = DRule(   1.8,  -1.0, 'M1 Wmin')
DR['M1.S1'] = DRule(   1.4,  -1.0, 'M1 Smin')
DR['M1.SC'] = DRule(  10.0,  -1.0, 'M1(C) Smin')
DR['M1.CO'] = DRule(   0.8,  -1.0, 'CO-M1 Fmin')
DR['M1.CC'] = DRule(   1.2,  -1.0, 'CO(C)-M1 Fmin')
DR['M1.WW'] = DRule(  10.0,  -1.0, 'M1(W) Wmin')
DR['M1.SW'] = DRule(   2.0,  -1.0, 'M1(W) Smin')
DR['V1.W1'] = DRule(   1.4,  -1.0, 'V1 Windth')
DR['V1.S1'] = DRule(   1.5,  -1.0, 'V1 Smin')
DR['V1.M1'] = DRule(   1.0,  -1.0, 'V1-M1 Emin')
DR['V1.PO'] = DRule(   1.2,  -1.0, 'V1-PO Smin')
DR['V1.CO'] = DRule(   1.0,  -1.0, 'V1-CO Smin')
DR['V1.CL'] = DRule(   1.4,  -1.0, 'V1-CO(L) Smin')
DR['M2.W1'] = DRule(   3.0,  -1.0, 'M2 Wmin')
DR['M2.S1'] = DRule(   2.0,  -1.0, 'M2 Smin')
DR['M2.V1'] = DRule(   1.0,  -1.0, 'V1-M2 Fmin')
