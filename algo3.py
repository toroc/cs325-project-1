
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



def maxSumSubarray_3(arr , low, high):
	"""
	Description:
	Input: array, index of 1st element, index of last element
	Output: Returns list containing max left index of first element 
		starting the subarray, max right index of last element in subarray, 
		and max sum of subarray made from left index to right index
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
		#Find the maximum subarray in the 1st half
		# ansLeft contains low idx, high idx, sum
		ansLeft = maxSumSubarray_3(arr, low, mid)

		#Find the maximum subarray in the 2nd half
		#ansRight contains low idx, high idx, sum
		ansRight = maxSumSubarray_3(arr, mid+1, high)

		#Find the maximum subarray within both halves
		#ansCross contains low idx, high idx, sum
		ansCross = maxCrossingSubarray(arr, low, mid, high)

		#Compare the max sums of the subarrays on the left, right, and middle
		#retun the list containing the max sum
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

	crossAns = maxLeft, maxRight, leftSum + rightSum
	# Return list contain left idx, right idx, and sum
	return crossAns

