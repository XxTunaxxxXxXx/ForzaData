#
#Math for the tune is from Diquee's of r/ForzaOpenTunes spreadsheet. Had an ongoing copy I made myself, and decided
#to evolve it into this to teach myself Python.
import variables
import functions
import sys

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
        functions.GetTuneInputs()
        print ('\nFront Spring: '+ str(round(variables.Tune['SpringFrontLb'],1)) + ' lb/in')
        print ('Rear Spring: '+ str(round(variables.Tune['SpringRearLb'],1)) + ' lb/in')
        print ('Front ARB: '+ str(round(variables.Tune['ArbFront'],1)))
        print ('Rear ARB: '+ str(round(variables.Tune['ArbRear'],1)))
        print ('Front Rebound: ' + str(round(variables.Tune['ReboundFront'],1)))
        print ('Rear Rebound: ' + str(round(variables.Tune['ReboundRear'],1)))
        print ('Front Bump: '+ str(round(variables.Tune['BumpFront'],1)))
        print ('Rear Bump: '+ str(round(variables.Tune['BumpRear'],1)))
        input ('Press any key to continue')
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
        input ('Press any key to continue')

    elif MenuSelection == '4': # Exit
        sys.exit('Thank you, come again.')
         


