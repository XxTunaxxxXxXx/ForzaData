import variables
import constants
import functions
import math


#get input for car variables
WeightLb = input('Car Weight in Lbs:\n')
FrontDist = float(input('Front Weight Percentage:\n'))*.01
Class = input('Car Class: D, C, B, A, S1, S2, or X\n')
SpringType = input('Spring Type: Rally, Race, or Drift\n')
DriveType = input('Drive Type: RWD, FWD, AWD\n')

DriveType = DriveType.upper()
SpringType = SpringType.upper()
Class = Class.upper()

#change weightlb to weightkgf
WeightKg = functions.lb_to_kg(WeightLb)
WeightKgf = functions.kg_to_kgf(WeightKg)

#Set front/back distribution
RearDist =  1 - FrontDist

#Set Min/Max Spring values and get the delta
SpringMaxFront = WeightKg * constants.Max_Front[SpringType]
SpringMinFront = WeightKg * constants.Min_Front[SpringType]
SpringMaxRear = WeightKg * constants.Max_Rear[SpringType]
SpringMinRear = WeightKg * constants.Min_Rear[SpringType]
variables.SpringFrontDelta = SpringMaxFront - SpringMinFront
variables.SpringRearDelta = SpringMaxRear - SpringMinRear


#Set Tune Spring Rates
#(WeightKgf)*WeightDistro*General
if DriveType == 'FWD':
    variables.Tune['SpringFront'] = functions.TuneSpring(WeightKgf,FrontDist,SpringType) * (1 - variables.DriveOffset)
    variables.Tune['SpringRear'] = functions.TuneSpring(WeightKgf,RearDist,SpringType)
elif DriveType() == 'RWD':
    variables.Tune['SpringFront'] = functions.TuneSpring(WeightKgf,FrontDist,SpringType)
    variables.Tune['SpringRear'] = functions.TuneSpring(WeightKgf,RearDist,SpringType) * (1 - variables.DriveOffset)
else :
    variables.Tune['SpringFront'] = functions.TuneSpring(WeightKgf,FrontDist,SpringType)
    variables.Tune['SpringRear'] = functions.TuneSpring(WeightKgf,RearDist,SpringType)


#Set Tune Anti-roll bars
variables.Tune['ArbFront'] = functions.TuneFront(constants.Arb_Delta_Front,variables.ArbFactor[Class])
variables.Tune['ArbRear'] =  functions.TuneRear(constants.Arb_Delta_Rear,variables.ArbFactor[Class])
    
#Set Rebound
variables.Tune['ReboundFront']= functions.TuneFront(constants.Rebound_Delta_Front, variables.ReboundFactor[SpringType])
variables.Tune['ReboundRear'] = functions.TuneRear(constants.Rebound_Delta_Front, variables.ReboundFactor[SpringType])

#Set Bump
variables.Tune['BumpFront'] = variables.Tune['ReboundFront'] * variables.BumpFactor[SpringType]
variables.Tune['BumpRear'] = variables.Tune['ReboundRear'] * variables.BumpFactor[SpringType]

#Set Brake

#print test
print ('Front Spring: '+ str(round(variables.Tune['SpringFront'],1)))
print ('Rear Spring: '+ str(round(variables.Tune['SpringRear'],1)))
print ('Front ARB: '+ str(round(variables.Tune['ArbFront'],1)))
print ('Rear ARB: '+ str(round(variables.Tune['ArbRear'],1)))
print ('Front Rebound: ' + str(round(variables.Tune['ReboundFront'],1)))
print ('Rear Rebound: ' + str(round(variables.Tune['ReboundRear'],1)))
print ('Front Bump: '+ str(round(variables.Tune['BumpFront'],1)))
print ('Rear Bump: '+ str(round(variables.Tune['BumpRear'],1)))