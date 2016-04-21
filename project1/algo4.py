import sys

def algo4(arr):
    """
    Linear Time version of the Maximum Sum Subarray

    Input: array
    Output: Returns max subarray and max sum in a tuple
    """

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
            
    return arr[low:high+1], maxSum   


