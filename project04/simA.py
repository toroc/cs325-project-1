#!usr/bin/env python
import math
import random
import time
import sys
import datetime

ABS_ZERO = 1e-4
COOL_RATE = .995

TEST_NODES = [(0,3,3),(1,2,2),(2,2,3),(3,1,4),(4,0,1),(5,3,3),(6,7,9),(7,0,2),(8,12,10)]


def greedyDavid(nodes, startNodeIndex, distTable):
	"""
	Description: Greedy algorithm with a local search heuristic to locate the closest neighbor node.
	Given an array of nodes to visit in the form (unique identifier, x-coord, y-coord), and an optional 
	starting node index (default is index 0), calculates a path to visit each node exactly once and return 
	to the starting node based on locating the closest unvisited node at each iteration.
	
	Input:
	nodes - an array of nodes in the form (unique identifier, x-coord, y-coord)
	startNodeIndex - optional parameter to identify the index of starting node in the array
	
	Output: Returns the total path distance and an array of nodes in the order visited

	Time Complexity:O(n^2)
	"""
	startNode = nodes[startNodeIndex]

	curNode = startNode
	visited = []				#empty list of visited nodes to start
	visited.append(startNode)
	unvisited = []	
	unvisited = nodes[:]		#copy of entire node list
	del unvisited[startNodeIndex]	#remove the start node from the list of visited nodes

	#loop until unvisited list is empty
	while len(unvisited) > 0:
		closestNode = unvisited[0]
		closestNodeDist = getCityDistance(curNode, closestNode, distTable)
		closestNodeIndex = 0

		for i in range(len(unvisited)):
			if getCityDistance(curNode, unvisited[i], distTable) < closestNodeDist:
				closestNode = unvisited[i]
				closestNodeDist = getCityDistance(curNode, closestNode, distTable)
				closestNodeIndex = i

		curNode = closestNode
		visited.append(curNode)
		del unvisited[closestNodeIndex]

	#visited.append(startNode) #return to the starting point
	#totalDist = pathDist(visited) #calculate the total path distance

	return visited		#return the total path distance and the path ordering
def readCoords1(inputFilename):
	coordFile = open(inputFilename, "r")

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

	coordFile.close()
	return cities, coords

def greedyStart(cities, distTable):
	minPath = []
	minCost = sys.maxsize

	for i in cities:

		curPath = []
		curPath.extend(greedyPath(cities, i, distTable))
		curCost = getPathCost(curPath, distTable)

		if curCost < minCost:
			minCost = curCost
			minPath = []
			minPath.extend(curPath)
		else:
			pass

	return minPath



def greedyPath(cities, i, distTable):
	"""Returns greedy path """

	greedyPath = []
	#neighbors = []
	totalPath = 0

	numCities = len(cities)
	available = []
	available.extend(cities)
	start = cities[i]
	currentCity = start
	greedyPath.append(start)
	

	currentCity = start
	#available.remove(start)
	#Find closest neighbors for each city

	while 0 < len(available):

		first, next, avg = getTwoNearest(available, currentCity,distTable)
		if first[0] != -1:
			#Take the greedy path most of the time
			if first[1] == next[1]:

				if (coinFlip3(0.6)):
					greedyPath.append(next[0])
					available.remove(currentCity)
					currentCity = next[0]
				else:
					greedyPath.append(first[0])
					available.remove(currentCity)
					currentCity = first[0]	   
			else:
				greedyPath.append(first[0])
				available.remove(currentCity)
				currentCity = first[0]
		else:
			available.remove(currentCity)

	return greedyPath


def getCityDistance(city1, city2, distTable):
	"""Returns distances of 2 cities from distance table
	"""

	if city1 < city2:
		#city2 = city2 - city1
		return distTable[city1][city2]
	else:
		#city1 = city1 - city2
		return distTable[city2][city1]


def getEuclDist(x1, x2, y1, y2):
	"""Returns euclidean(hypotenuse) distance between 2 cities
	"""
	distance = 0
	#math.sqrt((node2[2] - node1[2])**2 + (node2[1] - node1[1])**2)
	distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

	return distance


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




def swapCities(path, city1, city2):
	"""Returns path with swapped cities.

	"""

	i = city1
	j = city2
	swappedPath = []
	swappedPath.extend(path)
	swappedPath[i] = path[j]
	swappedPath[j] = path[i]
	
	assert swappedPath != path
	
	return swappedPath

def getRandomPath(cities):
	"""Returns a random path through all cities.
	"""
	available = []
	available.extend(cities)
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

	tlen = len(cities)-1
	city1 = random.randint(0,tlen)
	city2 = random.randint(0,tlen)
	while city1 == city2:
		city1 = random.randint(0,tlen)
		city2 = random.randint(0,tlen)
	return city1, city2

def getRandomCities2(cities):
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
	nextPath = []
	if start != end:
		
		nextPath.extend(cities)
		if start > end:
			nextPath[start + 1:] = reversed(cities[:end])
			nextPath[:end] = reversed(cities[start + 1:])
		else:
			nextPath[start:end + 1] = reversed(cities[start:end + 1])
		if nextPath != cities:
			return nextPath
			
def reversePathParts2(cities):

	start, end = getRandomCities2(cities)
	if start != end:
		nextPath = []
		nextPath = cities[:]
		if start > end:
			nextPath[start + 1:] = reversed(cities[:end])
			nextPath[:end] = reversed(cities[start + 1:])
		else:
			nextPath[start:end + 1] = reversed(cities[start:end + 1])
		if nextPath != cities:
			return nextPath


def coinFlip2(prevCost, nextCost, temp):


	diff = nextCost - prevCost
	p = math.exp(-(diff) / temp)
	u = random.random()
	#print("U: " + str(u) + "P: " + str(p))

	return u < p


def coinFlip(prevCost, nextCost, temp=7000):

	p = math.exp(-abs(nextCost - prevCost) / temp)
	u = random.random()
	return u > p


def coinFlip3(prob):
	u = 0
	u = random.random()
	return u > prob

#Uses greedyStart
def tspSimulated(cities, nodes):
	"""
	Input(s): cities - list of city ids, nodes - list of city ids with coordinates
	"""
	
	distanceTable = getDistanceTable(nodes)
	startPath = []
	#startPath = greedy2David(cities, nodes, distanceTable)
	randCities = []
	randCities = getRandomPath(cities)
	startPath = greedyStart(randCities, distanceTable)

	#use greedy to greedy path
	#print(greedyPath(startPath,distanceTable))
	#startPath = greedyPath(startPath,distanceTable)

	startCost = getPathCost(startPath, distanceTable)

	#return startTour, startCost
	minPath = []
	minPath = startPath
	minCost = 0
	minCost = startCost

	currentTemp = 10000

	while currentTemp > 0:

		# Improve the path
		city1, city2 = getRandomCities(cities)
		nextPath = []
		nextPath = swapCities(startPath, city1, city2)
		assert nextPath != startPath
		nextCost = getPathCost(nextPath, distanceTable)

		if nextCost < startCost:
			startPath = nextPath

			if nextCost < minCost:
				minCost = nextCost
				minPath = nextPath
		elif (coinFlip2(startCost, nextCost, currentTemp)):
			#print("coin flipped")
			startPath = nextPath
			startCost = nextCost
		else:
			pass
		
		currentTemp -= COOL_RATE

	return minCost, minPath


#Reverses parts of path instead of swapping

def tspSimulated3(cities, nodes):
	"""
	Input(s): cities - list of city ids, nodes - list of city ids with coordinates
	"""
	
	distanceTable = getDistanceTable(nodes)
	startPath = []
	#startPath = greedy2David(cities, nodes, distanceTable)
	randCities = []
	randCities.extend(getRandomPath(cities))
	startPath.extend(greedyStart(randCities, distanceTable))

	#use greedy to greedy path
	#print(greedyPath(startPath,distanceTable))
	#startPath = greedyPath(startPath,distanceTable)

	startCost = getPathCost(startPath, distanceTable)

	#return startTour, startCost
	minPath = []
	minPath.extend(startPath)
	minCost = 0
	minCost = startCost

	currentTemp = 10000

	while currentTemp > 0:

		# Improve the path
		#city1, city2 = getRandomCities(cities)
		nextPath = []
		nextPath.extend(reversePathParts(minPath))
		#nextPath = swapCities(startPath, city1, city2)
		#assert nextPath != startPath
		nextCost = getPathCost(nextPath, distanceTable)

		if nextCost < startCost:
			startPath = []
			startPath.extend(nextPath)

			if nextCost < minCost:
				minCost = nextCost
				minPath = []
				minPath.extend(nextPath)
		elif (coinFlip2(startCost, nextCost, currentTemp)):
			#print("coin flipped")
			startPath = []
			startPath.extend(nextPath)
			startCost = nextCost
		else:
			pass
		
		currentTemp -= COOL_RATE

	return minCost, minPath

#Uses regular greedy
def tspSimulated2(cities, nodes):
	"""
	Input(s): cities - list of city ids, nodes - list of city ids with coordinates
	"""
	
	distanceTable = getDistanceTable(nodes)
	startPath = []
	#startPath = greedy2David(cities, nodes, distanceTable)
	randCities = []
	randCities = getRandomPath(cities)
	startPath = greedyPath(randCities, 0, distanceTable)

	#use greedy to greedy path
	#print(greedyPath(startPath,distanceTable))
	#startPath = greedyPath(startPath,distanceTable)

	startCost = getPathCost(startPath, distanceTable)

	#return startTour, startCost
	minPath = []
	minPath = startPath
	minCost = 0
	minCost = startCost

	currentTemp = 30000

	while currentTemp > 0:

		# Improve the path
		city1, city2 = getRandomCities(cities)
		nextPath = []
		nextPath = swapCities(startPath, city1, city2)
		assert nextPath != startPath
		nextCost = getPathCost(nextPath, distanceTable)

		if nextCost < startCost:
			startPath = nextPath

			if nextCost < minCost:
				minCost = nextCost
				minPath = nextPath
		elif (coinFlip2(startCost, nextCost, currentTemp)):
			#print("coin flipped")
			startPath = nextPath
			startCost = nextCost
		else:
			pass
		
		currentTemp -= COOL_RATE

	return minCost, minPath

def tspSimA(cities, nodes):


	distanceTable = getDistanceTable(nodes)
	startPath = []
	#startPath = greedy2David(cities, nodes, distanceTable)
	randCities = []
	randCities = getRandomPath(cities)
	startPath = greedyStart(randCities, distanceTable)

	#use greedy to greedy path
	#print(greedyPath(startPath,distanceTable))
	#startPath = greedyPath(startPath,distanceTable)

	startCost = getPathCost(startPath, distanceTable)

	#return startTour, startCost
	minPath = []
	minPath = startPath
	minCost = 0
	minCost = startCost

	currentTemp = 1

	while currentTemp > ABS_ZERO:
		city1, city2 = getRandomCities(cities)
		nextPath = greedyPath(cities, city1, distanceTable)
		#nextPath = swapCities(startPath, city1, city2)
		assert nextPath != startPath
		nextCost = getPathCost(nextPath, distanceTable)

		if nextCost < startCost:
			startPath = nextPath

			if nextCost < minCost:
				minCost = nextCost
				minPath = nextPath
		elif (coinFlip2(startCost, nextCost, currentTemp)):
			#print("coin flipped")
			startPath = nextPath
			startCost = nextCost
		else:
			pass
		
		currentTemp *= COOL_RATE
		
	return minCost, minPath


def getTwoNearest(cities, curLoc, distTable):
	"""Returns ids and cost of the two closest citiest to current location,
	and average distance of cities to current location.
	"""
	city1Cost = sys.maxsize
	city2Cost = sys.maxsize
	city1 = -1
	city2 = -1
	avgDist = 0
	for i in cities:
		if i == curLoc:
			pass
		else:
			#Calculate cost from current location to this city
			cost = getCityDistance(curLoc, i, distTable)
			avgDist += cost

			if city1Cost > cost:
				city2Cost = city1Cost
				city1Cost = cost
				city2 = city1
				city1 = i
			elif city1Cost <= cost and city2Cost > cost :
				city2Cost = cost
				city2 = i
			else:
				pass

	avgDist = avgDist / len(cities)
	c1 = city1, city1Cost
	c2 = city2, city2Cost
	
	return  c1, c2, avgDist




random.seed(time.time())
inputFilename = "tsp_example_1.txt"



cities, nodes = readCoords1(inputFilename)


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

print("File # 1 ")
start = time.clock()
print(tspSimulated3(cities, nodes))
end = time.clock()
elapsed = end - start
print("Time elapsed is: " + str(elapsed))