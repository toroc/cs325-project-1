import processData, algo3, algo4

###############################TESTING OF ALGO3 #######################
myLists = processData.insertIntoArrays('MSS_TestProblems.txt')


for i in range(len(myLists)):
	testArray = myLists[i]
	testLen = len(testArray)-1

	# Test algo
	maxAns = algo3.maxSumSubarray_3(testArray, 0, testLen)
	leftIdx = maxAns[0]
	rightIdx = maxAns[1]

	fullArray = testArray
	subArray = testArray[leftIdx:rightIdx+1]
	maxSum = maxAns[2]

	processData.writeResults('algo3Results.txt', fullArray, subArray, maxSum)


###############################TESTING OF ALGO4 #######################
myLists = processData.insertIntoArrays('MSS_TestProblems.txt')


for i in range(len(myLists)):
	testArray = myLists[i]
	
	# Test algo
	maxAns = algo4.linMaxSubArray(testArray)
	leftIdx = maxAns[0]
	rightIdx = maxAns[1]

	fullArray = testArray
	subArray = testArray[leftIdx:rightIdx+1]
	maxSum = maxAns[2]

	processData.writeResults('algo4Results.txt', fullArray, subArray, maxSum)