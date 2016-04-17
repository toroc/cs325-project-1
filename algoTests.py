#!/usr/bin/python3.2
import processData
from algo1 import *
from algo2 import *
from algo3 import *
from algo4 import *



def runTests(fileName, algo, desc):
	"""
	Runs the algorithm correctness tests.
	Input: name of file, pointer to algorithm function to call, 
		and description of algorithm calling.
	Output: Correctness test results saved to MSS_Results.txt
	"""
	# Add test description to file

	file = open(fileName, "a")
	file.write("\n"+desc+"\n")


	myLists = processData.insertIntoArrays('MSS_Problems.txt')

	for i in range(len(myLists)):
		testArray = myLists[i]
		maxAns = algo(testArray)
		subArray = maxAns[0]
		maxSum = maxAns[1]
		processData.writeResults(file, testArray, subArray, maxSum)





# Run the tests
runTests('MSS_Results.txt', algo1, "Algorithm 1 Correctness Test Results: ")
runTests('MSS_Results.txt', algo2, "Algorithm 2 Correctness Test Results: ")
runTests('MSS_Results.txt', algo3, "Algorithm 3 Correctness Test Results: ")
runTests('MSS_Results.txt', algo4, "Algorithm 4 Correctness Test Results: ")


def getRunTimes(algo, desc, fileName, nList):
	"""

	"""
	

	# Get list of n

		# Repeat 10 times for each n
		
		# store array of n rand #s

		# set start time

		# run algo

		# set end time

		# calculate time

		# add to average time

	# calculate average running time

	# output results to fileName