#!usr/bin/env python
import math
import random
import time
import sys

ABS_ZERO = 1e-4
COOL_RATE = .85

TEST_NODES = [(0,3,3),(1,2,2),(2,2,3),(3,1,4),(4,0,1),(5,3,3),(6,7,9),(7,0,2),(8,12,10)]

def readCoords1(coordFile):
    cities = []
    coords = []
    for line in coordFile:
        parsed = line.strip().split(' ')
        #print(parsed)
        city = parsed[0]
        x = parsed[1]
        y = parsed[2]
        x = int(x)
        y = int(y)
        city = int(city)
        coords.append((city, x, y))
        cities.append(city)
    return cities, coords



def greedyPath(cities, distTable):

    greedyPath = list()
    neighbors = list()
    totalPath = 0

    numCities = len(cities)
    available = list(cities)
    start = cities[0]
    currentCity = start
    greedyPath.append(start)
    

    currentCity = start
    #Find closest neighbors for each city

    while 0 < len(available):

        first, next = getTwoNearest(available, currentCity,distTable)
        if first != -1:
            greedyPath.append(first)
            available.remove(currentCity)
            currentCity = first


    return greedyPath



    




def costDict(nodes):
    "Create dictionary with nodes as keys and distance as value"

    cost = {}

    for i, (id1, x1, y1) in enumerate(nodes):
        for j, (id1, x2, y2) in enumerate(nodes):
            dx, dy = x1 - x2, y1 - y2
            dist = hypot(x1 - x2, y1 - y2)
            #dist = sqrt(dx*dx + dy*dy)
            cost[i,j] = dist
    return cost


def getCityDistance(city1, city2, distTable):
    """Returns distances of 2 cities from distance table
    """

    if city1 < city2:
        city2 = city2 - city1
        return distTable[city1][city2]
    else:
        city1 = city1 - city2
        return distTable[city2][city1]


def getEuclDist(x1, x2, y1, y2):
    """Returns euclidean(hypotenuse) distance between 2 cities
    """
    a = (x1 - x2) ** 2
    b = (y1 - y2) ** 2
    c = int(round(math.sqrt(a + b)))

    return c


def getDistanceTable(nodes):
    """Returns table containing euclidean distances of cities
    Input: list of cities with x and y coordinates
    """

    # Convert into 2d matrix
    rows = cols = len(nodes)
    distTable = [[0 for x in range(cols)] for x in range(rows)]
    
    

    for i, (id1, x1, y1) in enumerate(nodes):
        for j, (id2, x2, y2) in enumerate(nodes):
            distTable[i][j] = getEuclDist(x1, x2, y1, y2)

    return distTable


def getPathCost(path, distTable):
    """Returns cost of path.
    """

    numCities = len(path)
    totalCost = 0
    i = 0

    while i < (numCities - 1):
        totalCost += getCityDistance(path[i], path[i + 1], distTable)
        i += 1

    #factor in cost from start to end
    totalCost += getCityDistance(path[numCities - 1], path[0], distTable)
    return totalCost


def getCost(tour, costMatrix):
    "Returns cost of tour"

    totalCost = 0
    tlen = len(tour) - 1
    #print(tlen)

    for i in range(tlen):
        #print(tour)
        thisNode = tour[i][0]
        n = i + 1
        nextNode = tour[i + 1][0]
        #print(tour)
        cost = costMatrix[thisNode,nextNode]
        totalCost = totalCost + cost
        #print(str(thisNode)+" -> " + str(nextNode) + " is " + str(cost) )

    # Cost of last to first
    firstNode = tour[0][0]
    lastNode = tour[tlen][0]
    cost = costMatrix[firstNode,lastNode]
    totalCost = totalCost + cost

    return totalCost


def nodePairs(nodes):

    n1 = nodes
    n2 = nodes
    shuffle = random.shuffle
    if shuffle:
        shuffle(n1)
        shuffle(n2)
    for i in n1:
        for j in n2:
            #print(i[0])
            #print(j[0])
            return i[0],j[0]



def swapCities(path, city1, city2):
    """Returns path with swapped cities.

    """

    swappedPath = list(path)
    swappedPath[city1] = path[city2]
    swappedPath[city2] = path[city1]
    return swappedPath




def randPairs(nodes):

    tlen = len(nodes)

    i = random.randint(0,tlen)
    j = (i + 1 + random.randint(0,tlen - 2)) % tlen

    if i > j:

        k = i
        i = j
        j = k
    return i, j



def getRandTour(nodes):
    "Returns random tour"
    # Make copy of list
    #Shuffle the list
    tour = list(nodes)
    random.shuffle(tour)

    return tour

def getRandomPath(cities):
    """Returns a random path through all cities.
    """
    available = list(cities)
    random.shuffle(available)
    numCities = len(cities)
    path = []
    curCount = 0
    while 0 < len(available):
        city = random.choice(available)
        available.remove(city)
        path.append(city)
        curCount += 1
    return path
    

def getRandomCities(cities):
    """Returns two random cities."""

    tlen = len(cities)
    city1 = random.randrange(0,tlen)
    city2 = random.randrange(0,tlen)
    while city1 == city2:
        city1 = random.randrange(0,tlen)
        city2 = random.randrange(0,tlen)
    return city1, city2


def reversePathParts(cities):

    start, end = getRandomCities(cities)
    if start != end:
        nextPath = list(cities)
        if start > end:
            nextPath[start+1:] = reversed(cities[:end])
            nextPath[:end] = reversed(cities[start+1:])
        else:
            nextPath[start:end+1] = reversed(cities[start:end+1])
        if nextPath != cities:
            yield nextPath
            



def coinFlip2(prevCost, nextCost, temp):


    diff = nextCost - prevCost
    p = math.exp(-(diff) / temp)
    u = random.random()
    #print("U: " + str(u) + "P: " + str(p))

    return u < p


def coinFlip(prevCost, nextCost, temp):

    if nextCost > prevCost:
        return True
    else:
        return exp(-(nextCost - prevCost) / temp)


def tspSimulated(cities, nodes):
    """
    Input(s): cities - list of city ids, nodes - list of city ids with coordinates
    """
    
    distanceTable = getDistanceTable(nodes)
    startPath = []
    startPath = getRandomPath(cities)

    #use greedy to greedy path
    #print(greedyPath(startPath,distanceTable))
    startPath = greedyPath(startPath,distanceTable)

    startCost = getPathCost(startPath, distanceTable)

    #return startTour, startCost
    minPath = startPath
    minCost = startCost

    currentTemp = 50

    while currentTemp > 0:

        # Improve the path
        city1, city2 = getRandomCities(cities)
        nextPath = swapCities(startPath, city1, city2)
        nextCost = getPathCost(nextPath, distanceTable)

        if nextCost < startCost:
            startPath = nextPath

            if nextCost < minCost:
                minCost = nextCost
                minPath = nextPath

        elif (coinFlip2(startCost, nextCost, currentTemp)):
            print("coin flipped")
            startPath = nextPath
            startCost = nextCost        
            
        currentTemp *= COOL_RATE

    return minCost, minPath
    # Use greedy algorithm for starting tour
    #minResult = greedy(startTour)
    #minPathDist = minResult[0]
    
    #costD = costDict(nodes)

    ## Initial tour
    #startTour = minResult[1]
    ##print("startTour: ")
    ##print(startTour)

    #minCost = minResult[0]
    #minTour = startTour
    ##tartTour = startTour

    ## Choose initial temperature
    #temp = 10

    #while temp > ABS_ZERO:

    #	randTour = getRandTour(startTour)
    #	#minRand = greedy(randTour)
    #	#randTour = minRand[1]
    #	randCost = pathDist(randTour)
    #	#print(randCost)
    #	startCost = pathDist(startTour)

    #	if randCost < startCost:
    #		startTour = randTour
    #		if randCost < minCost:
    #			minTour = randTour
    #			minCost = randCost
    #			#print("Mincost: " + str(minCost))
    #	elif (coinFlip2(startCost, randCost, temp)):
    #		#print("in coinFlip")
    #		#minRand = greedy(randTour)
    #		#randTour = minRand[1]
    #		startTour = randTour
        
    #	# Decrease Temp
    #	temp = temp * COOL_RATE
    #	#print(temp)


    #return minCost, minTour
def tspSimA(nodes):


    # Get a random start tour
    startTour = getRandTour(nodes)

    # Use greedy algorithm for starting tour
    minResult = greedy(startTour)
    minPathDist = minResult[0]
    
    costD = costDict(nodes)

    # Initial tour
    startTour = minResult[1]
    #print("startTour: ")
    #print(startTour)

    minCost = minResult[0]
    minTour = startTour
    #tartTour = startTour

    # Choose initial temperature
    temp = 10

    while temp > ABS_ZERO:

        randTour = getRandTour(startTour)
        #minRand = greedy(randTour)
        #randTour = minRand[1]
        randCost = pathDist(randTour)
        #print(randCost)
        startCost = pathDist(startTour)

        if randCost < startCost:
            startTour = randTour
            if randCost < minCost:
                minTour = randTour
                minCost = randCost
                #print("Mincost: " + str(minCost))
        elif (coinFlip2(startCost, randCost, temp)):
            #print("in coinFlip")
            #minRand = greedy(randTour)
            #randTour = minRand[1]
            startTour = randTour
        
        # Decrease Temp
        temp = temp * COOL_RATE
        #print(temp)


    return minCost, minTour

def getTwoNearest(cities, curLoc, distTable):
    """Returns ids of the two closest citiest to current location.
    """
    city1Cost = sys.maxsize
    city2Cost = sys.maxsize
    city1 = -1
    city2 = -1
    for i in cities:
        if i == curLoc:
            pass
        else:
            #Calculate cost from current location to this city
            cost = getCityDistance(curLoc, i, distTable)

            if city1Cost > cost:
                city2Cost = city1Cost
                city1Cost = cost
                city2 = city1
                city1 = i
            elif city1Cost <= cost  and city2Cost > cost :
                city2Cost = cost
                city2 = i
    return city1, city2







# DEBUG / TESTING
def readCoords(coordFile):
    coords = []
    for line in coordFile:
        parsed = line.strip().split(' ')
        #print(parsed)
        city = parsed[0]
        x = parsed[1]
        y = parsed[2]
        x = int(x)
        y = int(y)
        city = int(city)
        coords.append((city, x, y))
    return coords


random.seed(time.clock())
inputFilename = "tsp_example_1.txt"


file = open(inputFilename, "r")
cities, nodes = readCoords1(file)


#------------------------------------------------------------
#   Helper functions to
#
#
#------------------------------------------------------------

#------------------------------------------------------------
#  TEST individual functions
#
#
#------------------------------------------------------------
start = time.clock()
print(tspSimulated(cities, nodes))
end = time.clock()
elapsed = end - start
print("Time elapsed is: " + str(elapsed))