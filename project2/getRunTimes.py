
#!usr/bin/env python

import os
import time
from changeSlow import *
from changegreedy import *
from changedp import *

    
def runAlgoTimes(algo, testString, startAmount, incrementFactor, denom, maxR):


    print(testString)

    for i in range(maxR):
        amount = startAmount + (i * incrementFactor)
        start = time.clock()
        coinsUsed = algo(denom, amount)[0]
        end = time.clock()
        elapsedTime = end - start
        print(str(amount)+" : "+ str(coinsUsed) +" : "+str(elapsedTime))


def getRunTimes():

    algos = [changegreedy, changedp]

    for algo in algos:
        testString = "Q4. Run Times for "+str(algo)
        startAmount = 2010
        incrementFactor = 5
        denominations = [1,5,10,25,50]
        runAlgoTimes(algo, testString, startAmount, incrementFactor, denominations, 39)

    for algo in algos:
        testString = "Q5. with denom1: Run Times for "+str(algo)
        startAmount = 2000
        incrementFactor = 1
        denominations = [1,2,6,12,24,48,60]
        runAlgoTimes(algo, testString, startAmount, incrementFactor, denominations, 201)

    for algo in algos:
        testString = "Q5. with denom2: Run Times for "+str(algo)
        startAmount = 2000
        incrementFactor = 1
        denominations = [1,6,13,37,150]
        runAlgoTimes(algo, testString, startAmount, incrementFactor, denominations, 201)

    for algo in algos:
        testString = "Q6. Run Times for "+str(algo)
        startAmount = 2000
        incrementFactor = 1
        denominations = [1,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
        runAlgoTimes(algo, testString, startAmount, incrementFactor, denominations, 201)   

##########################################################################################################################
"""
The algorithms above were used for answering questions related to project 2.  
"""
##########################################################################################################################
getRunTimes()