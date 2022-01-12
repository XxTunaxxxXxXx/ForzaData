import variables
import constants
import sys
#import only system from os for screen clear
from os import system, name

#lb to kg
def lb_to_kg(unit):
    if checkfloat(unit):
        unit = float(unit)
        unit /= 2.205
        return unit
    else:
        print("lb_to_kg input was not valid float. Functions line 14\n")
        sys.exit("Input to function was:" + unit)
#kg to kg/f
def kg_to_kgf(unit):
    if checkfloat(unit):
        unit = float(unit)
        unit *= 0.1
        return unit
    else:
        print("kg_to_kgf input was not valid float. Functions line 23\n")
        sys.exit("Input to function was:" + unit)
#kgf to n/mm
def kgf_to_nmm(unit):
    if checkfloat(unit):
        unit = float(unit)
        unit /= constants.nmm_to_kgf
        return unit
    else:
        print("kgf_to_nmm input was not valid float. Functions line 32\n")
        sys.exit("Input to function was:" + unit)
#n/mm to lb/in
def nmm_to_lbin(unit):
    if checkfloat(unit):
        unit = float(unit)
        unit *= constants.nmm_to_lbin
        return unit
    else:
        print("nmm_to_lbin input was not valid float. Functions line 41\n")
        sys.exit("Input to function was:" + unit)
    
#Check if input is float
def checkfloat(x):
    try:
        float(x)
        return True
    except:
        return False
    
#TuneSpring, TuneFront, and TuneRear are all used in the TuneCar function. 
#Set Spring rates, Weight needs to be in kfg, Distribution is for weight distribution,Spring is Spring type. Output will be kgf
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
    
#Takes Weight in Kg, Type of Spring, Front Weight Distsribution, Car Class, and Drive type and sets base Tune 
def TuneCar(WeightKg, SpringType, FrontDist, CarClass, DriveType):
    try:
        #Get kg/f weight for spring calculations
        WeightKgf = kg_to_kgf(WeightKg)
        #Set Min/Max Spring values and get the delta
        SpringMaxFront = WeightKg * constants.Max_Front[SpringType]
        SpringMinFront = WeightKg * constants.Min_Front[SpringType]
        SpringMaxRear = WeightKg * constants.Max_Rear[SpringType]
        SpringMinRear = WeightKg * constants.Min_Rear[SpringType]
        variables.SpringFrontDelta = SpringMaxFront - SpringMinFront
        variables.SpringRearDelta = SpringMaxRear - SpringMinRear
        #Set rear weight distribution,
        FrontDist *= .01
        RearDist =  round(1 - FrontDist,2)
        
        #Set Tune Spring Rates
        if DriveType == 'FWD':
            variables.Tune['SpringFrontKgf'] = TuneSpring(WeightKgf,FrontDist,SpringType) * (1 - variables.DriveOffset)
            variables.Tune['SpringRearKgf'] = TuneSpring(WeightKgf,RearDist,SpringType)
        elif DriveType == 'RWD':
            variables.Tune['SpringFrontKgf'] = TuneSpring(WeightKgf,FrontDist,SpringType)
            variables.Tune['SpringRearKgf'] = TuneSpring(WeightKgf,RearDist,SpringType) * (1 - variables.DriveOffset)
        else :
            variables.Tune['SpringFrontKgf'] = TuneSpring(WeightKgf,FrontDist,SpringType)
            variables.Tune['SpringRearKgf'] = TuneSpring(WeightKgf,RearDist,SpringType)

        #set Spring units for each metric
        variables.Tune['SpringFrontNmm'] = kgf_to_nmm(variables.Tune['SpringFrontKgf'])
        variables.Tune['SpringRearNmm'] = kgf_to_nmm(variables.Tune['SpringRearKgf'])
        variables.Tune['SpringFrontLb'] = nmm_to_lbin(variables.Tune['SpringFrontNmm'])
        variables.Tune['SpringRearLb'] = nmm_to_lbin(variables.Tune['SpringRearNmm'])
        print (str(variables.Tune['SpringFrontKgf'])+'\n')
        print (str(variables.Tune['SpringRearKgf'])+'\n')
        print (str(variables.Tune['SpringFrontNmm'])+'\n')
        print (str(variables.Tune['SpringRearNmm'])+'\n')
        print (str(variables.Tune['SpringFrontLb'])+'\n')
        print (str(variables.Tune['SpringRearLb'])+'\n')
        
        
        #Set Tune Anti-roll bars, Rebound, and Bump
        if SpringType.upper() == "RALLY" or SpringType.upper() == "STOCK BUGGY":
            variables.Tune['ArbFront'] = TuneFront(constants.Arb_Delta_Front,variables.ArbFactor[CarClass])*variables.ArbRallyFactor
            variables.Tune['ArbRear'] =  TuneRear(constants.Arb_Delta_Rear,variables.ArbFactor[CarClass])*variables.ArbRallyFactor
            variables.Tune['ReboundFront']= TuneFront(constants.Rebound_Delta_Front, variables.ReboundFactor[SpringType])
            variables.Tune['ReboundRear'] = TuneRear(constants.Rebound_Delta_Rear, variables.ReboundFactor[SpringType])
            variables.Tune['BumpFront'] = variables.Tune['ReboundFront'] * variables.BumpFactor[SpringType]
            variables.Tune['BumpRear'] = variables.Tune['ReboundRear'] * variables.BumpFactor[SpringType]   
        else:
            variables.Tune['ArbFront'] = TuneFront(constants.Arb_Delta_Front,variables.ArbFactor[CarClass])
            variables.Tune['ArbRear'] =  TuneRear(constants.Arb_Delta_Rear,variables.ArbFactor[CarClass])
            variables.Tune['ReboundFront']= TuneFront(constants.Rebound_Delta_Front, variables.ReboundFactor[SpringType])
            variables.Tune['ReboundRear'] = TuneRear(constants.Rebound_Delta_Rear, variables.ReboundFactor[SpringType])
            variables.Tune['BumpFront'] = variables.Tune['ReboundFront'] * variables.BumpFactor[SpringType]
            variables.Tune['BumpRear'] = variables.Tune['ReboundRear'] * variables.BumpFactor[SpringType]   
        return True
    except Exception as e:
        print(e)
        sys.exit('Error occured on Tune function')

# clear screen 
def screen_clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')