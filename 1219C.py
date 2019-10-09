import math
period = int(input(""))
number = int(input(""))
potency = period-1
def repeater(string, numTimes):
    return int(string*numTimes)

if(len(str(number)) > period):
    calculated = '1'+potency*'0'
    calculated = int(calculated)
    #calculated = # int(str(number)[:period])
    numRepetitions =len(str(number))/float(period)
    numRepetitions = int(math.ceil(numRepetitions))
   # calculated = repeater(str(calculated), numRepetitions)
    sw = True
    sw2 = False
    if(int(repeater(str(calculated),numRepetitions)) > number):
        sw2 = True
        #calculated = calculated +1
        #calculated = repeater(str(calculated),numRepetitions)
        #print(calculated,2)
        #print(numRepetitions,2)
    # print(calculated)
    if(sw2 == False):
        calculated = str(number)[:period]
        calculated = int(calculated)
    while(sw):
        if(int(repeater(str(calculated),numRepetitions)) > number):
            sw = False
        if((calculated+1) == int('1'+period*'0')):
            calculated = '1'+potency*'0'
            numRepetitions = numRepetitions +1
            sw = False
        calculated = int(calculated) +1
        # print(str(calculated)+"dddd")

    calculated = repeater(str(calculated-1), numRepetitions)

if(len(str(number)) < period):
    calculated = '1'+potency*'0'

if(len(str(number)) == period):
    calculated = '1'+potency*'0'
    calculated = int(calculated)
    sw = True
    numRepetitions = 1
    calculated = number

    while(sw):
        calculated = calculated +1

        #numberCalculated = str(calculated)
        if(int(repeater(str(calculated),numRepetitions)) > number):
            sw = False
        if(calculated == int('1'+period*'0')):
            numRepetitions = numRepetitions +1
            sw = False
    calculated = repeater(str(calculated), numRepetitions)
print(calculated)
