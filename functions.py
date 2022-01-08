import variables
import constants

def lb_to_kg(unit):
    unit = float(unit)
    unit /= 2.205
    return unit

def kg_to_kgf(unit):
    unit = float(unit)
    unit *= 0.1
    return unit
    
def kgf_to_nmm(unit):
    unit = float(unit)
    unit *= 1
    return unit
    
    
#Set Spring rates, Weight needs to be in kfg, Distribution is for weight distribution,Type is Spring type
#(WeightKgf)*WeightDistro*General
def TuneSpring(Weight,Distribution,Spring):
    result = Weight * Distribution * variables.SpringFactor[Spring]
    return result

#Input Part Delta, then part factor. Needs to be ran after SpringFront is calculated. For Arb and Rebound
def TuneFront(Delta,Factor):
    result = (variables.Tune['SpringFront'] / variables.SpringFrontDelta * Delta) * Factor
    return result

#Input Part Delta, then part factor. Needs to be ran after SpringRear is calculated. For Arb and Rebound
def TuneRear(Delta,Factor):
    result = (variables.Tune['SpringRear'] / variables.SpringRearDelta * Delta) * Factor
    return result
