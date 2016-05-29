#!usr/bin/env python
from math import *
import random


TEST_NODES = [(1,2,2),(2,2,3),(3,1,4),(4,0,1),(5,3,3),(6,7,9),(7,0,2),(8,12,10)]


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

	print(cost)

	return cost



def getRandTour(nodes):
	"Returns random tour"

	# Make copy of list
	tour = list(nodes)
	#Shuffle the list
	random.shuffle(tour)

	return tour


def tspSimA(nodes):

	costD = costDict(TEST_NODES)

	# Initial tour
	minCost = getCost(nodes)
	minTour = nodes

	

	# Choose initial temperature
	temp = 0.1;



# DEBUG / TESTING
costD = costDict(TEST_NODES)

print(costD)


tourCost = getCost(TEST_NODES, costD)

randTour = getRandTour(TEST_NODES)
randCost = getCost(randTour, costD)

print("Initial Tour: " + str(tourCost))
print("Random Tour: " + str(randCost))