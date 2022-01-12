#
#Math for the tune is from Diquee's of r/ForzaOpenTunes spreadsheet. Had an ongoing copy I made myself, and decided
#to evolve it into this to teach myself Python.
import variables
import functions
import sys

         
#Quick script to get needed input and error check before putting through to TuneCar. 
def GetTuneInputs():
    #screen_clear()
    Weight = input('Car Weight in '+ variables.WeightUnit +': ')
    while True:
        if functions.checkfloat(Weight):
            Weight = float(Weight)
            break
        else:
            Weight = input('Please input a valid Car Weight in '+ variables.WeightUnit + ': ')
    #screen_clear()
    FrontDist = input('Front Weight Percentage: ')
    while True:
        if functions.checkfloat(FrontDist):
            FrontDist = float(FrontDist)
            if FrontDist >= 1 and FrontDist <= 100:
                FrontDist = float(FrontDist)
                break
        FrontDist = input('Please input a valid weight percentage, 1-100: ')
    #screen_clear()
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
    #screen_clear()
    while True:
        DriveType = input('Drive Type - RWD, FWD, AWD: ')
        types = ['FWD','AWD','RWD']
        if DriveType.upper() in types:
            DriveType = DriveType.upper()
            break
        else:
            print ('Please input a valid drive type - RWD, FWD, AWD: ')
    #Tune car
    if variables.WeightUnit == 'Lbs':
        functions.TuneCar(functions.lb_to_kg(Weight), SpringType, FrontDist, CarClass, DriveType)
    else:
        functions.TuneCar(Weight, SpringType, FrontDist, CarClass, DriveType)


#get input for car variables and set tune
while True:
    print('Please choose an option:')
    functions.screen_clear()
    print('1. Set base tune')
    print('2. Change weight unit, currently using ' +  variables.WeightUnit)
    print('3. Show last tune')
    print('4. Exit')
    
    MenuChoices = ['1','2','3', '4']
    MenuSelection = input('Enter Selection:')
    while True:
        if MenuSelection in MenuChoices:
            break
        else:
            functions.screen_clear()
            print('1. Set base tune')
            print('2. Change weight unit, currently using ' +  variables.WeightUnit)
            print('3. Change variables')
            print('4. Exit')
            MenuSelection = input ('Please input a valid selection, 1-4: ')

    if MenuSelection == '1': # Set base tune
        functions.screen_clear()
        GetTuneInputs()
        functions.screen_clear()
        print ('\nFront Spring: '+ str(round(variables.Tune['SpringFrontLb'],1)) + ' lb/in')
        print ('Rear Spring: '+ str(round(variables.Tune['SpringRearLb'],1)) + ' lb/in')
        print ('Front ARB: '+ str(round(variables.Tune['ArbFront'],1)))
        print ('Rear ARB: '+ str(round(variables.Tune['ArbRear'],1)))
        print ('Front Rebound: ' + str(round(variables.Tune['ReboundFront'],1)))
        print ('Rear Rebound: ' + str(round(variables.Tune['ReboundRear'],1)))
        print ('Front Bump: '+ str(round(variables.Tune['BumpFront'],1)))
        print ('Rear Bump: '+ str(round(variables.Tune['BumpRear'],1)))
        print ('\nFor AWD road tunes, it\'s advised to used Front ARB of 1-5, and Rear ARB of 60-65 and adjust from there as needed')
        input ('\nPress enter to continue')
        input ('Press enter to continue')
    elif MenuSelection == '2': # Change weight unit
        if variables.WeightUnit == 'Lbs':
            variables.WeightUnit = 'Kgs'
        else:
            variables.WeightUnit = 'Lbs'
    elif MenuSelection == '3': #Print tune again
        functions.screen_clear()
        print ('Front Spring: '+ str(round(variables.Tune['SpringFrontLb'],1)) + ' lb/in')
        print ('Rear Spring: '+ str(round(variables.Tune['SpringRearLb'],1)) + ' lb/in')
        print ('Front ARB: '+ str(round(variables.Tune['ArbFront'],1)))
        print ('Rear ARB: '+ str(round(variables.Tune['ArbRear'],1)))
        print ('Front Rebound: ' + str(round(variables.Tune['ReboundFront'],1)))
        print ('Rear Rebound: ' + str(round(variables.Tune['ReboundRear'],1)))
        print ('Front Bump: '+ str(round(variables.Tune['BumpFront'],1)))
        print ('Rear Bump: '+ str(round(variables.Tune['BumpRear'],1)))
        print ('\nFor AWD road tunes, it\'s advised to used Front ARB of 1-5, and Rear ARB of 60-65 and adjust from there as needed')
        input ('\nPress enter to continue')

    elif MenuSelection == '4': # Exit
        sys.exit('Thank you, come again.')
