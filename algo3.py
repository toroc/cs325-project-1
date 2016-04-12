
#!/usr/bin/python3.2

#------------------------------------------------------------
# CS 325 - Spring 2016 - Project 1
#   By: Carol Toro
#   File Created: 4/11/2016
#   Last Modified: 4/11/2016
#   Filename: algo3.py

import sys
import math
sys.setrecursionlimit(10000)



def maxSumSubarray_3(arr , low, high):
	"""
	Description:
	Input:
	Output: 
	"""
	sumIdx = 2
	#Base Case: only 1 element
	if high == low:
		#print(low)
		base = low, high, arr[low]
		return base
	else:
		#print(low)
		#print(high)
		# Get mid point of array
		mid = math.floor((low+high)/2)

		#print(mid)
		# ansLeft contains low idx, high idx, sum
		ansLeft = maxSumSubarray_3(arr, low, mid)
		#ansRight contains low idx, high idx, sum
		ansRight = maxSumSubarray_3(arr, mid+1, high)

		#ansCross contains low idx, high idx, sum
		ansCross = maxCrossingSubarray(arr, low, mid, high)

		if ansLeft[sumIdx] >= ansRight[sumIdx] and ansLeft[sumIdx] >= ansCross[sumIdx]:	
			return ansLeft
		elif ansRight[sumIdx] >= ansLeft[sumIdx] and ansRight[sumIdx] >= ansCross[sumIdx]:
			return ansRight
		else:
			return ansCross



def maxCrossingSubarray(arr , low, mid, high):
	"""
	Description:
	Input:
	Output: 
	"""
	leftSum = -100000
	totalSum = 0

	i = mid
	maxLeft=0
	maxRight=0

	while i >= low:
		totalSum = totalSum + arr[i]

		if totalSum > leftSum:
			leftSum = totalSum
			maxLeft = i

		i= i - 1

	rightSum = -100000
	totalSum = 0

	j = mid + 1

	while j <= high:

		totalSum = totalSum + arr[j]

		if totalSum > rightSum:
			rightSum = totalSum;
			maxRight = j

		j = j + 1

	crossAns = maxLeft, maxRight, leftSum + rightSum
	return crossAns


# Inserted this function into file for testing purposes
# once we have all algos completed, we can automate the calls to each algo
def insertIntoArrays():
    """
    Description: 
        Reads data from text file
        Converts each line in file into array of integers
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


    #print(arrayList)
    #print(arrayList[0]) 
    #print(arrayList[1])   
    
    return arrayList



myLists = insertIntoArrays()

testList = myLists[0]
testLen = len(testList)-1
print(myLists[0])

maxAns = maxSumSubarray_3(testList, 0, testLen)

leftIdx = maxAns[0]
rightIdx = maxAns[1]
maxSum = maxAns[2]


#Print subarray
print(testList[leftIdx:rightIdx+1])


print("HELLO\n")
