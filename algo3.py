
#!/usr/bin/python3.2

#------------------------------------------------------------
# CS 325 - Spring 2016 - Project 1
#   By: Carol Toro
#   File Created: 4/11/2016
#   Last Modified: 4/11/2016
#   Filename: algo3.py

import sys
import math
import processData
sys.setrecursionlimit(10000)

def algo3(arr):

	return maxSubarray_3(arr, 0, len(arr)-1)



def maxSubarray_3(arr, low, high):
	"""
	Divide and Conquer Version of the Maximum Sum Subarray
	Description:
	Input: array, index of 1st element, index of last element
	Output: Returns max subarray and max sum in a tuple
	"""
	sumIdx = 1
	#Base Case: only 1 element
	if high == low:
		base = arr[low:high+1], arr[low]
		return base
	else:

		# Get mid point of array
		mid = (int((low+high)/2))

		#Find the maximum subarray in the 1st half
		# ansLeft contains subarray with sum
		ansLeft = maxSubarray_3(arr, low, mid)

		#Find the maximum subarray in the 2nd half
		#ansRight contains subarray with sum
		ansRight = maxSubarray_3(arr, mid+1, high)

		#Find the maximum subarray within both halves
		#ansCross contains subarray with sum
		ansCross = maxCrossingSubarray(arr, low, mid, high)

		#Compare the max sums of the subarrays on the left, right, and middle
		#return the list containing the max sum
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
	Output: Returns the subarray and sum 
	"""
	leftSum = -100000
	totalSum = 0

	i = mid
	maxLeft=0
	maxRight=0

	# Get the max sum left of the middle
	while i >= low:
		totalSum = totalSum + arr[i]

		if totalSum > leftSum:
			leftSum = totalSum
			maxLeft = i

		i= i - 1

	rightSum = -100000
	totalSum = 0

	j = mid + 1

	# Get the max sum right of the middle
	while j <= high:

		totalSum = totalSum + arr[j]

		if totalSum > rightSum:
			rightSum = totalSum;
			maxRight = j

		j = j + 1

	crossAns = arr[maxLeft:maxRight+1], leftSum + rightSum
	# Return list contain subArray and sum
	return crossAns

