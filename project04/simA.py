#!usr/bin/env python
from math import *
import random
import sys
import greedy_tsp

ABS_ZERO = 1e-4
COOL_RATE = 0.999

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

	cost = 0;
	tlen = len(tour)-1

	for i in range(0,tlen-1):
		
		thisNode = tour[i][0]
		nextNode = tour[i+1][0]
		cost = cost + costMatrix.get(thisNode,nextNode)

	# Cost of last to first
	firstNode = tour[0][0]
	lastNode = tour[tlen][0]
	cost = cost + costMatrix.get(firstNode, lastNode)

	return cost



def getRandTour(nodes):
	"Returns random tour"

	# Make copy of list
	tour = list(nodes)
	#Shuffle the list
	random.shuffle(tour)

	return tour

def coinFlip(prevCost, nextCost, temp):

	if nextCost > prevCost:
		return 1.0
	else:
		return exp(-abs(nextCost-prevCost)/ temp)


def tspSimA(nodes):

	costD = costDict(TEST_NODES)

	# Initial tour
	minCost = getCost(nodes, costD)
	minTour = nodes
	startTour = nodes

	# Choose initial temperature
	temp = 0.1;

	while temp > ABS_ZERO:

		randTour = getRandTour(startTour)
		randCost = getCost(randTour, costD)
		startCost = getCost(startTour, costD)

		if randCost < startCost:
			startTour = randTour

			if randCost < minCost:
				minTour = randTour
				minCost = randCost
		elif (coinFlip(startCost, randCost, temp)):
			startTour = randTour

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



inputFilename = "tsp_example_1.txt"

file = open(inputFilename, "r")
nodes = readCoords(file)
print(tspSimA(nodes))
print(greedy_tsp.greedy(nodes))