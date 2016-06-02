#!usr/bin/env python
import math

TEST_NODES = [(1,2,2),(2,2,3),(3,1,4),(4,0,1),(5,3,3),(6,7,9),(7,0,2),(8,12,10)]


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


def greedy2(nodes):
    """
    Description: Uses greedy() to find a closest-neighbor path that visites each node in 
    an array of nodes exactly once.  Iterates through the list of nodes using each 
    node as a starting node, and determines which path yielded the minimum path distance.
    
    Input:
    nodes - an array of nodes in the form (unique identifier, x-coord, y-coord)
    
    Output: Returns the total path distance and an array of nodes in the order visited

    Time Complexity:O(n^3)
    """
    minResult = greedy(nodes)
    minPathDist = minResult[0]

    for i in range(len(nodes) - 1):
        result = greedy(nodes, i)
        if result[0] < minPathDist:
            minResult = result
            minPathDist = result[0]

    return minResult


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
	#distance = 0
	#distance = int(round(math.sqrt((node2[2] - node1[2])**2 + (node2[1] - node1[1])**2)))
	#return distance

	distance = 0
    	distance = int(round((math.sqrt((node2[2] - node1[2])**2 + (node2[1] - node1[1])**2))))
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


def testDist():
	"""
	Description: Testing for dist()
	"""
	print("TEST dist() FUNCTION")
	dist0_1 = dist(TEST_NODES[0],TEST_NODES[1])
	print("Distance from (2,2) to (2,3): " + str(dist0_1))
	dist2_4 = dist(TEST_NODES[2], TEST_NODES[4])
	print("Distance from (1,4) to (3,3): " + str(dist2_4))


def testPathDist():
    """
	Description: Testing for pathDist()
	"""
    print("TEST pathDist() FUNCTION")
    pathDistTestNodes = pathDist(TEST_NODES)
    print("Path distance of testNodes in order: " + str(pathDistTestNodes))


def testGreedy():
	"""
	Description: Testing for greedy()
	"""
	print("TEST greedy() FUNCTION")
	print("Greedy Algorithm on testNodes, start index = 0:")
	print(greedy(TEST_NODES))
	print("Greedy Algorithm on testNodes, start index = 3:")
	print(greedy(TEST_NODES, 3))
	print(greedy(TEST_NODES, 3)[0])

	print("TEST greedy() FUNCTION FROM ALL STARTING POINTS")
	#use greedy() to determine closest path using each node as a start node
	for i in range(len(TEST_NODES) - 1):
		print("Start Index: " + str(i))
		print(greedy(TEST_NODES, i))

	print("TEST greedy2() FUNCTION")
	print(greedy2(TEST_NODES))


def testGreedy2():
    print("TEST greedy2() FUNCTION")
    print(greedy2(TEST_NODES))


def runTests():
	print("Test Nodes:")
	print(TEST_NODES)
	testDist()
	print
	testPathDist()
	print
	testGreedy()
	print
	testGreedy2()


#runTests()
