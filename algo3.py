import sys
import math
sys.setrecursionlimit(10000)


def maxSumSubarray_3(arr, low, high):

	#Base Case: only 1 element
	if high == low:
		return low, high, arr[low]
	else:

		mid = math.floor((low+high/2))

		leftLow, leftHigh, leftSum = 
		ansLeft = maxSumSubarray_3(arr, low, mid)

		rightLow, rightHigh, rightSum = maxSumSubarray_3(arr, mid+1, high)
		ansRight = maxSumSubarray_3(arr, mid+1, high)

		crossLow, crossHigh, crossSum = maxCrossingSubarray(arr, low, mid, high)
		ansCross = maxCrossingSubarray(arr, low, mid, high)

		if leftSum >= rightSum and leftSum >= crossSum:	
			return ansLeft
		elif rightSum >= leftSum and rightSum >= crossSum:
			return ansRight
		else:
			answer = crossLow, crossHigh, crossSum
			return ansCross



def maxCrossingSubarray(arr, low, mid, high):

	leftSum = -10000
	totalSum = 0

	i = mid
	maxLeft=0
	maxRight=0

	while i > low:
		totalSum = totalSum + arr[i]

		if totalSum > leftSum:
			leftSum = totalSum
			maxLeft = i

		i= i - 1

	rightSum = -100000
	totalSum = 0

	j = mid + 1

	while j < high:

		totalSum = totalSum + arr[j]

		if totalSum > rightSum:
			rightSum = totalSum;
			maxRight = j

		j = j + 1


	return maxLeft, maxRight, leftSum + rightSum



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

    with open('MSS_Problems.txt') as file:
        for line in file:
            #Get rid of brackets and empty space    
            line = line.replace('[', '').replace(' ', '').replace(']', '')

            #Append each number to list, add comma separator for next list
            arrayList.append([int(num) for num in line.split(',') if num not in '\n'])


    #print(arrayList)
    #print(arrayList[0]) 
    #print(arrayList[1])   
    
    return arrayList



myList = insertIntoArrays()
listLen = len(myList[1])
print(listLen)

maxL, maxR, maxS = maxSumSubarray_3(myList[1], 0, listLen)

print(maxL)
print(maxR)
print(maxS)
print("HELLO\n")
