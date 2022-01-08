#varGeneral =
#varRebound =
#varBump =
#varARB =
#varBrake Offset =

#SpringActiveMax =
#=IF('Tune Calculator'!$B$6="Race",J8, If('Tune Calculator'!$B$6="Rally",J10,J12))
#SpringActiveMin =


#ArbFactor = {"D":0.50,"C":0.60,"B":0.70,"A":0.80,"S1":0.90,"S2":1.0,"X":1.0}
#SpringFactor = {"RALLY":100,"RACE":200,"DRIFT":200}
#ReboundFactor = {"RALLY":60,"RACE":100,"DRIFT":100}
#BumpFactor = {"RALLY":50,"RACE":60,"DRIFT":60}

ArbFactor = {"D":0.50,"C":0.60,"B":0.70,"A":0.80,"S1":0.90,"S2":1.0,"X":1.0}
SpringFactor = {"RALLY":1,"RACE":2,"DRIFT":2}
ReboundFactor = {"RALLY":.60,"RACE":1,"DRIFT":1}
BumpFactor = {"RALLY":.35,"RACE":.60,"DRIFT":.60}
DriveOffset = .04
BrakeOffset = .01


#Blank tune dictionary, mainly for reference, SpringFront/Rear will be in Kfg by default
Tune = {"SpringFront":0, "SpringRear":0, "ArbFront":0, "ArbRear":0, "ReboundFront":0, "ReboundRear":0, "BumpFront":0,"BumpRear":0}


#Setting variables outside of main to reference easily in functions
DriveType = 'RWD'
SpringType = 'Rally'
Class = 'A'
SpringRearDelta = 0
SpringFrontDelta = 0
