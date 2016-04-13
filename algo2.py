
def maxSumSubarray_2(arr=[]):
    """
    Description: Algorithm 2 - Better Enumeration
        Computes the sum of all possible subarrays by adding the next value in the array to
        the previously computed sum.
    Input: arr - an array of ints
    Output: Returns the start index of the subarray, end index of the subarray, and the sum of the subarray
    Complexity: O(n^2)
    """

    #if the array is empty, return 0
    if len(arr) == 0:
        return []
    
    #if the array only has one element, return that element
    elif len(arr) == 1:
        return arr[0]

    maxSum = arr[0]  #the largest sum of a subarray of arr
    start = 0        #the beginning index for a subarray of arr
    stop = 0         #the end index for a subarray arr
    curSum = 0       #stores the sum of the current subarray of arr

    #compute the sum for all possible pairs of indices (i,j) such that 0<=i<j
    for i in range(len(arr) - 1):
        curSum = arr[i]                    #resets the value of curSum each time i increments
        for j in range(i + 1, len(arr)):
            curSum += arr[j]
            if curSum > maxSum:
                start = i
                stop = j
                maxSum = curSum

    #check to see if the last element in arr is larger than all other subarray sums
    #i.e. like for the array [-2,-5,-11,5]
    if arr[len(arr) - 1] > maxSum:
        maxSum = arr[len(arr) - 1]
        start = len(arr) - 1
        stop = len(arr) - 1

    return start, stop, maxSum
