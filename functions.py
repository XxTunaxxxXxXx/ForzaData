import variables
import constants
import sys

#lb to kg
def lb_to_kg(unit):
    if checkfloat(unit):
        unit = float(unit)
        unit /= 2.205
        return unit
    else:
        print("lb_to_kg input was not valid float. An exception has occured\n")
        sys.exit("Input to function was:" + unit)
#kg to kg/f
def kg_to_kgf(unit):
    if checkfloat(unit):
        unit = float(unit)
        unit *= 0.1
        return unit
    else:
        print("kg_to_kgf input was not valid float. An exception has occured\n")
        sys.exit("Input to function was:" + unit)
#kgf to n/mm
def kgf_to_nmm(unit):
    if checkfloat(unit):
        unit = float(unit)
        unit /= constants.nmm_to_kgf
        return unit
    else:
        print("kgf_to_nmm input was not valid float. An exception has occured\n")
        sys.exit("Input to function was:" + unit)
#n/mm to lb/in
def nmm_to_lbin(unit):
    if checkfloat(unit):
        unit = float(unit)
        unit *= constants.nmm_to_lbin
        return unit
    else:
        print("nmm_to_lbin input was not valid float. An exception has occured\n")
        sys.exit("Input to function was:" + unit)
    
#Check if input is float
def checkfloat(x):
    try:
        float(x)
        return True
    except:
        return False
    
#Set Spring rates, Weight needs to be in kfg, Distribution is for weight distribution,Type is Spring type.
#Output will be kgf
def TuneSpring(Weight,Distribution,Spring):
    result = Weight * Distribution * variables.SpringFactor[Spring]
    return result

#Input Part Delta, then part factor. Needs to be ran after SpringFront is calculated. For Arb and Rebound
def TuneFront(Delta,Factor):
    result = (variables.Tune['SpringFrontKgf'] / variables.SpringFrontDelta * Delta) * Factor
    return result

#Input Part Delta, then part factor. Needs to be ran after SpringRear is calculated. For Arb and Rebound
def TuneRear(Delta,Factor):
    result = (variables.Tune['SpringRearKgf'] / variables.SpringRearDelta * Delta) * Factor
    return result
