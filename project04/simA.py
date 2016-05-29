#!usr/bin/env python
from math import *
import random
from datetime import datetime
import sys


ABS_ZERO = 1e-4
COOL_RATE = 0.9999

TEST_NODES = [(0,3,3),(1,2,2),(2,2,3),(3,1,4),(4,0,1),(5,3,3),(6,7,9),(7,0,2),(8,12,10)]


def costDict(nodes):
	"Create dictionary with nodes as keys and distance as value"

	cost={}

	for i, (id1, x1, y1) in enumerate(nodes):
		for j, (id1, x2, y2) in enumerate(nodes):
			dx, dy = x1-x2, y1-y2
			dist = sqrt(dx*dx + dy*dy)
			cost[i,j] = dist
	return cost



def getCost(tour, costMatrix):
	"Returns cost of tour"

	totalCost = 0;
	tlen = len(tour)-1
	#print(tlen)

	for i in range(tlen):
		#print(tour)
		thisNode = tour[i][0]
		n = i +1
		nextNode = tour[i+1][0]
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
			yield (i[0],j[0])


def swapNodes(nodes):

	for i,j in nodePairs(nodes):
		#print(i)
		#print(j)
		if i < j:
			tourCopy = list(nodes)

			tourCopy[i] = nodes[j]
			tourCopy[j] = nodes[i]
			return tourCopy


def getRandTour(nodes):
	"Returns random tour"
	# Make copy of list
	#Shuffle the list
	tour  = nodes
	random.shuffle(tour)

	return tour

def coinFlip(prevCost, nextCost, temp):

	p = exp(-(nextCost-prevCost)/ temp)
	u = random.uniform(0,1)
	#print("U: " + str(u) + "P: " + str(p))

	if u > p:
		return True
	else:
		return False



def getCities(nodes):

	cities = []
	for i, (id1,x1,x2) in enumerate(nodes):
		city = id1
		cities.append(city)

	return cities

def tspSimA(nodes):

	costD = costDict(nodes)

	# Initial tour
	startTour = getRandTour(nodes)

	minCost = getCost(startTour, costD)
	minTour = startTour
	startTour = startTour

	# Choose initial temperature
	temp = 10;

	while temp > ABS_ZERO:

		randTour = getRandTour(startTour)
		randCost = getCost(randTour, costD)
		startCost = getCost(startTour, costD)

		if randCost < startCost:
			startTour = randTour

			if randCost < minCost:
				minTour = randTour
				minCost = randCost
				#print("Mincost: " + str(minCost))

		elif (coinFlip(startCost, randCost, temp)):
			#print("in coinFlip")
			startTour = randTour
		
		# Decrease Temp
		temp = temp * COOL_RATE
		#print(temp)


	return minCost, minTour





# DEBUG / TESTING



# costD = costDict(TEST_NODES)

# #print(costD)


# tourCost = getCost(TEST_NODES, costD)

# randTour = getRandTour(TEST_NODES)
# randCost = getCost(randTour, costD)

# print("Initial Tour: " + str(tourCost))
# print("Random Tour: " + str(randCost))

# print(tspSimA(TEST_NODES))


import sys

def readCoords(coordFile):
	coords=[]
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


random.seed(datetime.now())
inputFilename = "tsp_example_1.txt"


file = open(inputFilename, "r")
nodes = readCoords(file)
print(tspSimA(nodes)) 

#print(getCities(nodes))
# print(greedy_tsp.greedy2(nodes))

#costD = costDict(TEST_NODES)

# print(costD)
# print(getCost(TEST_NODES, costD))
#print(swapNodes(nodes))
