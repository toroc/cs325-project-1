from algo1 import *
from algo2 import *
import random
import time

MIN_RANDOM_INT = -100
MAX_RANDOM_INT = 100
ALGO_1_START = 100
INCREMENT_ALGO_1 = 100
ALGO_2_START = 1000
INCREMENT_ALGO_2 = 500
NUM_TESTS = 10

def generateRandomArray(n):
    """
    Generate an array of n random ints between -100 and 100 
    """
    randomArray = []
    
    for i in range(n):
        randomArray.append(random.randint(MIN_RANDOM_INT, MAX_RANDOM_INT))

    return randomArray


def algoAnalysis(algorithm, n):
    """
    Tests the runtime of an algorithm 10 times, and computes the average of the 10 tests
    returns the average runtime of the funciton
    """
    runTimes = []
    elapsedTime = 0
    totalTime = 0
    avgTime = 0

    for i in range(NUM_TESTS):
        currentArray = generateRandomArray(n)
        start = time.clock()
        algorithm(currentArray)
        end = time.clock()
        elapsedTime = end - start
        totalTime += elapsedTime

    avgTime = totalTime

    return avgTime / NUM_TESTS
    
def runTests():
    """
    Runs execution time tests on algorithm 1 and algorithm 2
    Uses custom input sizes for each algorithm
    Prints the test array size and the avg. runtime for 10 different input sizes
    """

    #Test algorithm 1
    print("Algorithm 1 Test Results:")
    for i in range(10):
        testSize = TEST_ARRAY_START + (INCREMENT_ALGO_1 * i)
        print("Array Size: " + str(testSize))
        print("Avg. Runtime: " + str(algoAnalysis(algo1, testSize)))

    #Test algorithm 2
    print("\n\nAlgorithm 2 Test Results:")
    for i in range(10):
        testSize = ALGO_2_START + (INCREMENT_ALGO_2 * i)
        print("Array Size: " + str(testSize))
        print("Avg. Runtime: " + str(algoAnalysis(algo2, testSize)))

    







        
