#!usr/bin/env python
import math
import random
import time
import sys
import datetime

ABS_ZERO = 1e-4
COOL_RATE = .995
HIGH_TEMP = 175000
MEDIUM_HIGH = 100000
MEDIUM_TEMP = 10000
MEDIUM_LOW = 3000
LOW_TEMP = 200
COIN_PROB = 0.6
random.seed(time.time())

def readCoords1(inputFilename):
	coordFile = open(inputFilename, "r")

	cities = list()
	coords = list()
	for line in coordFile:
		parsed = line.strip().split()
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
	"""Returns a path

	"""
	minGreedyPath = list()
	minCost = sys.maxsize

	for i in cities:

		curPath = list()
		curPath.extend(greedyPath(cities, i, distTable))
		curCost = getPathCost(curPath, distTable)

		if curCost < minCost:
			minCost = curCost
			minGreedyPath = list()
			minGreedyPath.extend(curPath)
		else:
			pass

	del curPath
	return minGreedyPath



def greedyPath(cities, i, distTable):
	"""Returns greedy path for city at position i. 
	Input: list of cities, index of starting city, 2d matrix containing 
	euclidean distances of cities.
	
	"""

	greedyPath = list()
	totalPath = 0

	numCities = len(cities)
	available = list()
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
				# When two cities are equally away in distance from the current city,
				# 1 - COIN_PROB that the second city is chosen.

				if (coinFlip3(COIN_PROB)):
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
	Input: index of 2 cities and 2d matrix containing euclidean distance.
	"""
	return distTable[city2][city1]


def getEuclDist(x1, x2, y1, y2):
	"""Returns euclidean(hypotenuse) distance between 2 cities
	"""
	distance = 0
	#a^2+b^2 = c^20
	#distance = math.hypot(x1 - x2, y1 - y2)
	dx, dy = x1 - x2, y1 - y2
	distance =int(round(math.sqrt((dx*dx) + (dy*dy))))
	
    #dist = sqrt(dx*dx + dy*dy)
	#math.sqrt((node2[2] - node1[2])**2 + (node2[1] - node1[1])**2)
	#distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

	return distance


def getDistanceTable(nodes):
	"""Returns table containing euclidean distances of cities
	Input: list of cities with x and y coordinates
	"""

	# Convert into 2d matrix
	rows = cols = len(nodes)
	distTable = [[0 for x in range(cols)] for y in range(rows)]
	
	
	for i, (id1, x1, y1) in enumerate(nodes):
		for j, (id2, x2, y2) in enumerate(nodes):
			distTable[i][j] = getEuclDist(x1, x2, y1, y2)

	#print(distTable)
	return distTable


def getPathCost(path, distTable, done=False):
	"""Returns cost of path.
	"""

	numCities = len(path)
	totalCost = 0
	i = 0

	while i < (numCities - 1):
		cityDist = getCityDistance(path[i], path[i + 1], distTable)
		#if done:
			#print(str(path[i]) + " -> " + str(path[i + 1]) + " = " + str(cityDist))
		totalCost += cityDist
		i += 1

	#factor in cost from start to end
	totalCost += getCityDistance(path[numCities - 1], path[0], distTable)
	return totalCost




def swapCities(path, city1, city2):
	"""Returns path with swapped cities.

	"""

	i = city1
	j = city2
	swappedPath = list()
	swappedPath.extend(path)
	swappedPath[i] = path[j]
	swappedPath[j] = path[i]
	
	assert swappedPath != path
	
	del path
	return swappedPath

def getRandomPath(cities):
	"""Returns a random path through all cities.
	"""
	available = list()
	available.extend(cities)
	random.shuffle(available)
	numCities = len(cities)
	path = list()
	curCount = 0
	while 0 < len(available):
		city = random.choice(available)
		available.remove(city)
		path.append(city)
		curCount += 1
	return path
	

def getRandomCities(cities):
	"""Returns two random cities."""

	tlen = len(cities) - 1
	city1 = 0
	city2 = 0
	city1 = random.randint(0,tlen)
	city2 = random.randint(0,tlen)
	while city1 == city2:
		city1 = random.randint(0,tlen)
		city2 = random.randint(0,tlen)
	return city1,city2

def getRandomCities2(cities):
	"""Returns two random cities not including the first city."""

	tlen = len(cities)
	city1 = random.randrange(0,tlen)
	city2 = random.randrange(0,tlen)
	while city1 == city2:
		city1 = random.randrange(0,tlen)
		city2 = random.randrange(0,tlen)
	return city1, city2


def reversePathParts(cities):
	"""Returns a path with certain parts of the original path reversed."""

	start, end = getRandomCities(cities)
	nPath = list()		
	nPath.extend(cities)
	if start > end:
		nPath[start + 1:] = reversed(cities[:end])
		nPath[:end] = reversed(cities[start + 1:])
	else:
		nPath[start:end + 1] = reversed(cities[start:end + 1])
	
	return nPath


def coinFlip2(prevCost, nextCost, temp):
	"""Returns a coin flip."""
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




#Reverses parts of path instead of swapping
def tspSimulated(cities, nodes):
	"""
	Input(s): cities - list of city ids, nodes - list of city ids with coordinates
	Starts with random path and then uses greedy path to find best path from random 
	starting point.
	"""
	
	distanceTable = getDistanceTable(nodes)
	startPath = list()
	randCities = list()
	randCities.extend(getRandomPath(cities))
	startPath.extend(greedyStart(randCities, distanceTable))

	startCost = getPathCost(startPath, distanceTable)

	#return startTour, startCost
	minPath = list()
	minPath.extend(startPath)
	minCost = 0
	minCost = startCost

	currentTemp = 0
	currentTemp = getStartTemperature(cities)
	#print("\t Starting Temp of " + str(currentTemp))

	while currentTemp > 0:

		# Improve the path
		#city1, city2 = getRandomCities(cities)
		nextPath = list()
		nextPath.extend(reversePathParts(minPath))
		#nextPath = swapCities(startPath, city1, city2)
		#assert nextPath != startPath
		nextCost = getPathCost(nextPath, distanceTable)

		if nextCost < startCost:
			startPath = list()
			startPath.extend(nextPath)

			if nextCost < minCost:
				minCost = nextCost
				minPath = list()
				minPath.extend(nextPath)
				del nextPath
		elif (coinFlip2(startCost, nextCost, currentTemp)):
			#print("coin flipped")
			startPath = list()
			startPath.extend(nextPath)
			startCost = nextCost
			del nextPath
		else:
			pass
		
		currentTemp -= COOL_RATE

	#endCost = getPathCost(minPath,distanceTable, True)
	#print(endCost)
	#print(minPath)
	return minCost, minPath
	
	
def tspSimulated2(cities, nodes):
	"""
	Input(s): cities - list of city ids, nodes - list of city ids with coordinates
	Starts with random path and then uses greedy path to find best path from random 
	starting point.
	Uses greedy path without greedy start
	"""
	
	distanceTable = getDistanceTable(nodes)
	startPath = list()
	#startPath = greedy2David(cities, nodes, distanceTable)
	randCities = list()
	randCities.extend(getRandomPath(cities))
	startPath.extend(greedyPath(randCities,0, distanceTable))

	startCost = getPathCost(startPath, distanceTable)

	minPath = list()
	minPath.extend(startPath)
	minCost = 0
	minCost = startCost

	currentTemp = getStartTemperature(cities)
	#print("\t Starting Temp of " + str(currentTemp))

	while currentTemp > 0:

		# Improve the path
		#city1, city2 = getRandomCities(cities)
		nextPath = list()
		nextPath.extend(reversePathParts(minPath))
		#nextPath = swapCities(startPath, city1, city2)
		#assert nextPath != startPath
		nextCost = getPathCost(nextPath, distanceTable)

		if nextCost < startCost:
			startPath = list()
			startPath.extend(nextPath)

			if nextCost < minCost:
				minCost = nextCost
				minPath = list()
				minPath.extend(nextPath)
				del nextPath
		elif (coinFlip2(startCost, nextCost, currentTemp)):
			#print("coin flipped")
			startPath = list()
			startPath.extend(nextPath)
			startCost = nextCost
			del nextPath
		else:
			pass
		
		currentTemp -= COOL_RATE

	return int(minCost), minPath


def getStartTemperature(cities):

	numCities = len(cities)

	if numCities < 2000:
		return HIGH_TEMP
	elif numCities < 5000:
		return MEDIUM_HIGH
	elif numCities < 7000:
		return MEDIUM_TEMP
	else:
		return MEDIUM_LOW



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



#Trials for competition files
'''
for i in range(1,8):
	inputFilename = "tsp_test_cases/test-input-" + str(i) + ".txt"
	cities, nodes = readCoords1(inputFilename)
	print(inputFilename)
	
	for j in range(20):
		
		if len(cities) >= 1000:
			start = time.clock()
			cost, tour = tspSimulated2(cities, nodes)
			end = time.clock()
			elapsed = end - start
			print("Trial #:" + str(j + 1)+ "\t" + str(cost) + "\t" + str(elapsed))
			#print(tour)
		else:
			start = time.clock()
			cost, tour = tspSimulated(cities, nodes)
			end = time.clock()
			elapsed = end - start
			print("Trial #:" + str(j + 1)+ "\t" + str(cost) + "\t" + str(elapsed))
			#print(tour)
'''
#inputFilename = "tsp_test_cases/test-input-5.txt"
#cities, nodes = readCoords1(inputFilename)
#start = time.clock()
#costTable = getDistanceTable(nodes)
#tour = greedyStart(cities, costTable)
#cost = getPathCost(tour, costTable)
#end = time.clock()
#print("\t Tour Cost: " + str(cost))
#elapsed = end - start
#print("\t Time elapsed is: " + str(elapsed))