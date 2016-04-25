#!usr/bin/env python

def changegreedy(denominations, amount):
    """
    Description: Greedy algorithm to calculate the number of coins necesarry to make
    change for the given parameter.  Makes as much change as possible with the highest
    denomination coin, and then moves to the next smaller coin and repeats the process
    until the amount is reached.  This is a naive algorithm and does not return the
    optimal solution for all variations of coin denominations.  This algorithm does always
    return an optimal solution for U.S. coin currency consisting of pennies, nickels, dimes,
    and quarters.
    
    Input:
    array denominations - an array of the different possible denominations of coins
        Array of denomiantions must be ascending order, with the first element value = 1
    int amount - the number of cents to make change for
    
    Output: an array in the form [numQuarters, numDimes, numNickels, numPennies] necessary
    to make change for the amount parameter

    O(n): Iterates one time through the list of denominations
    """
    results = []

    #increment from the end of the array toward the front; array is in ascending order
    for i in range(len(denominations) - 1, -1, -1):
        
        #use as many of the largest coins possible
        numCoins = amount // denominations[i]
        results.insert(0, numCoins)

        #subtract the amount made with the largest denomination
        amount -= (numCoins * denominations[i])


    coinsUsed = sum(results)
    return coinsUsed, results
        
