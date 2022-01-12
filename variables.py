#If you feel a need to customize how the car is tuned in any way, treat these as % multipliers for each part. 
ArbFactor = {
    "D":0.50,
    "C":0.60,
    "B":0.70,
    "A":0.80,
    "S1":0.90,
    "S2":1.0,
    "X":1.0
    }
SpringFactor = {
    "RALLY":1.0,
    "STOCK BUGGY":.60,
    "RACE":2.0,
    "DRIFT":2.0
    }
ReboundFactor = { 
    "STOCK BUGGY":.60,
    "RALLY":0.60,
    "RACE":1.0,
    "DRIFT":1.0
    }
BumpFactor = {
    "RALLY":0.35,
    "STOCK BUGGY":.35,
    "RACE":0.60,
    "DRIFT":0.60
    }
    
DriveOffset = .04  # Softens drive suspension
ArbRallyFactor = .65 # Softens ARB for rally/offroad builds

WeightUnit = 'Lbs' # For weight toggle input on ForzaTerminal.py

#Blank tune dictionary
Tune = {
    "SpringFrontKgf":0,
    "SpringFrontNmm":0,
    "SpringFrontLb":0,
    "SpringRearKgf":0,
    "SpringRearNmm":0,
    "SpringRearLb":0,
    "ArbFront":0,
    "ArbRear":0,
    "ReboundFront":0,
    "ReboundRear":0,
    "BumpFront":0,
    "BumpRear":0
    }
