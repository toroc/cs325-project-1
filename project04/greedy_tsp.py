#!usr/bin/env python
import math

def greedy(nodes, startNodeIndex = 0):
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
    #if startNodeIndex == None:
    #	startNode = nodes[0]
    #else:
    
    startNode = nodes[startNodeIndex];

    curNode = startNode
    visited = []				#empty list of visited nodes to start
    visited.append(startNode)	
    unvisited = nodes[:]		#copy of entire node list
    del unvisited[startNodeIndex]	#remove the start node from the list of visited nodes

    #loop until unvisited list is empty
    while len(unvisited) > 0:
        closestNode = unvisited[0]
        closestNodeDist = dist(curNode, closestNode)
        closestNodeIndex = 0

        for i in range(len(unvisited)):
            if dist(curNode, unvisited[i]) < closestNodeDist:
                closestNode = unvisited[i]
                closestNodeDist = dist(curNode, closestNode)
        		closestNodeIndex = i

        curNode = closestNode
        visited.append(curNode)
        del unvisited[closestNodeIndex]

    visited.append(startNode)		#return to the starting point
    totalDist = pathDist(visited)	#calculate the total path distance

    return totalDist, visited		#return the total path distance and the path ordering


def dist(node1, node2):
    """
    Description: Calculates the straight-line distance between two points in a 
    2-dimensional plane.
    
    Input:
    node1 - a node in the form (unique identifier, x-coord, y-coord)
    node2 - a node in the form (unique identifier, x-coord, y-coord)
    
    Output: Returns the straight-line distance between node1 and node2

    Time Complexity: O(1)
    """
    distance = 0
    distance = math.sqrt((node2[2] - node1[2])**2 + (node2[1] - node1[1])**2)
    return distance


def pathDist(path):
	"""
    Description: Calculates the total distance of a given path of nodes in the 
    form (unique identifier, x-coord, y-coord)
    
    Input:
    path - a list of nodes in order of travel (index 0 to index len(path)-1)
    
    Output: Returns the total path distance rounded to the nearest int

    Time Complexity: O(n)
    """
	totalDist = 0
	for i in range(len(path) - 1):
		totalDist += dist(path[i], path[i + 1])

	return int(totalDist)


def testGreedy():
	"""
	Description: Testing for greedy(), dist(), and pathDist()
	"""
	testNodes = [(1,2,2),(2,2,3),(3,1,4),(4,0,1),(5,3,3)]
	print("TEST dist() FUNCTION")
	dist0_1 = dist(testNodes[0],testNodes[1])
	print("Distance from (2,2) to (2,3): " + str(dist0_1))
	dist2_4 = dist(testNodes[2], testNodes[4])
	print("Distance from (1,4) to (3,3): " + str(dist2_4))
	print
	print("TEST pathDist() FUNCTION")
	pathDistTestNodes = pathDist(testNodes)
	print("Path distance of testNodes in order: " + str(pathDistTestNodes))
	print
	print("TEST greedy() FUNCTION")
	print("Greedy Algorithm on testNodes, start index = 0:")
	print(greedy(testNodes))
	print("Greedy Algorithm on testNodes, start index = 3:")
	print(greedy(testNodes, 3))
	print

	print("TEST greedy() FUNCTION FROM ALL STARTING POINTS")
    #use greedy() to determine closest path using each node as a start node
	for i in range(len(testNodes) - 1):
		print("Start Index: " + str(i))
		print(greedy(testNodes, i))



testGreedy()
