import sys

def linMaxSubArray(arr):
    n = len(arr)
    currentSum = 0
    maxSum = 0
    low = 0
    high = 0
    for i in range(n):
        currentHigh = i
        if currentSum > 0:
            currentSum += arr[i]
        else:
            currentLow = i
            currentSum = arr[i]
        if currentSum > maxSum:
            maxSum = currentSum
            low = currentLow
            high = currentHigh
    return low, high, maxSum   

def insertIntoArrays():
    """
    Description: 
        Reads data from text file Converts each line in file into array of integers
        Appends next array to list of arrays
    Input: n/a 
    Output: Returns array of arrays (list of arrays)
    """

    arrayList = []

    with open('MSS_TestProblems.txt') as file:
        for line in file:
            #Get rid of brackets and empty space    
            line = line.replace('[', '').replace(' ', '').replace(']', '')

            #Append each number to list, add comma separator for next list
            arrayList.append([int(num) for num in line.split(',') if num not in '\n'])  
    return arrayList


###############################TESTING OF ALGO4 #######################
myLists = insertIntoArrays()

for i in range(len(myLists)):
    testList = myLists[i]
    #testLen = len(testList)-1
    print(myLists[i])
    
    maxAns = linMaxSubArray(testList)
    leftIdx = maxAns[0]
    rightIdx = maxAns[1]
    maxSum = maxAns[2]

    #Print subarray
    print(testList[leftIdx:rightIdx+1])
    print(maxSum)
		