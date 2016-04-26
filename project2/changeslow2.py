#!usr/bin/env python

MAX_INT = 10000000000

def changeslow(denominations, amount):
    if amount == 0:
        return 0

    numCoins = MAX_INT
    
    #I was using this block of code to try to create the array of necessary coins of each denomination
    #results = []
    #for i in range(len(denominations)):
    #    results.append(0)

    for i in range(len(denominations)):
        if denominations[i] <= amount:
            #print("Trying: " + str(denominations[i]) + " cent coin: " + str(numCoins + 1))      #used for testing
            numCoins = min(changeslow(denominations, amount - denominations[i]) + 1, numCoins)

    return numCoins
