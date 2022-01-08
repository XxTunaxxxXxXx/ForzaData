#
#Math for the tune is from Diquee's of r/ForzaOpenTunes spreadsheet. Had an ongoing copy I made myself, and decided
#to evolve it into this to teach myself Python.

import variables
import constants
import functions
import math


#get input for car variables
WeightLb = input('Car Weight in Lbs: ')
while True:
    if functions.checkfloat(WeightLb):
        WeightLb = float(WeightLb)
        break
    else:
        WeightLb = input('Please input a valid Car Weight in Lbs: ')

FrontDist = input('Front Weight Percentage: ')
while True:
    if functions.checkfloat(FrontDist):
        FrontDist = float(FrontDist)
        if FrontDist >= 1 and FrontDist <= 100:
            FrontDist = float(FrontDist)*.01
            RearDist =  round(1 - FrontDist,2)
            break
    else:
        FrontDist = input('Please input a valid weight percentage, 1-100: ')

CarClass = input('Car Class - D, C, B, A, S1, S2, or X: ')
while True:
    if CarClass.upper() in variables.ArbFactor.keys():
        CarClass = CarClass.upper()
        break
    else:
        CarClass = input ('Please input a valid Car Class -  D, C, B, A, S1, S2, or X: ')

SpringType = input('Spring Type - Rally, Race, or Drift: ')
while True:
    if SpringType.upper() in variables.SpringFactor.keys():
        SpringType = SpringType.upper()
        break
    else:
        SpringType = input ('Please input a valid spring type - Rally, Race, or Drift: ')

while True:
    DriveType = input('Drive Type - RWD, FWD, AWD: ')
    types = ['FWD','AWD','RWD']
    if DriveType.upper() in types:
        DriveType = DriveType.upper()
        break
    else:
        print ('Please input a valid drive type - RWD, FWD, AWD: ')
    


#set variables for weight in kg and weight in kgf
WeightKg = functions.lb_to_kg(WeightLb)
WeightKgf = functions.kg_to_kgf(WeightKg)



#Set Min/Max Spring values and get the delta
SpringMaxFront = WeightKg * constants.Max_Front[SpringType]
SpringMinFront = WeightKg * constants.Min_Front[SpringType]
SpringMaxRear = WeightKg * constants.Max_Rear[SpringType]
SpringMinRear = WeightKg * constants.Min_Rear[SpringType]
variables.SpringFrontDelta = SpringMaxFront - SpringMinFront
variables.SpringRearDelta = SpringMaxRear - SpringMinRear


#Set Tune Spring Rates
if DriveType == 'FWD':
    variables.Tune['SpringFrontKgf'] = functions.TuneSpring(WeightKgf,FrontDist,SpringType) * (1 - variables.DriveOffset)
    variables.Tune['SpringRearKgf'] = functions.TuneSpring(WeightKgf,RearDist,SpringType)
elif DriveType == 'RWD':
    variables.Tune['SpringFrontKgf'] = functions.TuneSpring(WeightKgf,FrontDist,SpringType)
    variables.Tune['SpringRearKgf'] = functions.TuneSpring(WeightKgf,RearDist,SpringType) * (1 - variables.DriveOffset)
else :
    variables.Tune['SpringFrontKgf'] = functions.TuneSpring(WeightKgf,FrontDist,SpringType)
    variables.Tune['SpringRearKgf'] = functions.TuneSpring(WeightKgf,RearDist,SpringType)

#set Spring units for each metric
variables.Tune['SpringFrontNmm'] = functions.kgf_to_nmm(variables.Tune['SpringFrontKgf'])
variables.Tune['SpringRearNmm'] = functions.kgf_to_nmm(variables.Tune['SpringRearKgf'])

variables.Tune['SpringFrontLb'] = functions.nmm_to_lbin(variables.Tune['SpringFrontNmm'])
variables.Tune['SpringRearLb'] = functions.nmm_to_lbin(variables.Tune['SpringRearNmm'])


#Set Tune Anti-roll bars
variables.Tune['ArbFront'] = functions.TuneFront(constants.Arb_Delta_Front,variables.ArbFactor[CarClass])
variables.Tune['ArbRear'] =  functions.TuneRear(constants.Arb_Delta_Rear,variables.ArbFactor[CarClass])
    
#Set Rebound
variables.Tune['ReboundFront']= functions.TuneFront(constants.Rebound_Delta_Front, variables.ReboundFactor[SpringType])
variables.Tune['ReboundRear'] = functions.TuneRear(constants.Rebound_Delta_Front, variables.ReboundFactor[SpringType])

#Set Bump
variables.Tune['BumpFront'] = variables.Tune['ReboundFront'] * variables.BumpFactor[SpringType]
variables.Tune['BumpRear'] = variables.Tune['ReboundRear'] * variables.BumpFactor[SpringType]

#Set Brake


print ('\n\n')
print ('Front Spring: '+ str(round(variables.Tune['SpringFrontLb'],1)) + ' lb/in')
print ('Rear Spring: '+ str(round(variables.Tune['SpringRearLb'],1)) + ' lb/in')
print ('Front ARB: '+ str(round(variables.Tune['ArbFront'],1)))
print ('Rear ARB: '+ str(round(variables.Tune['ArbRear'],1)))
print ('Front Rebound: ' + str(round(variables.Tune['ReboundFront'],1)))
print ('Rear Rebound: ' + str(round(variables.Tune['ReboundRear'],1)))
print ('Front Bump: '+ str(round(variables.Tune['BumpFront'],1)))
print ('Rear Bump: '+ str(round(variables.Tune['BumpRear'],1)))

