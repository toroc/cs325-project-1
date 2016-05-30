#!usr/bin/env python
import math
import greedy_tsp


def greedyPeek(nodes, startNodeIndex = 0):
    """
    Description: uses a look-ahead technique to improve upon the results of the closest neighbor algorithm
    for the TSP.  When choosing the next node to travel to, the algorithm compares the distance from the 
    current node to the next two nodes, and chooses the next node based on the shortest 2-node path from 
    the unvisited nodes.
    
    Input:
    nodes - an array of nodes in the form (unique identifier, x-coord, y-coord)
    startNodeIndex - optional parameter to identify the index of starting node in the array
    
    Output: Returns the total path distance and an array of nodes in the order visited

    Time Complexity: O(n^3)
    """
    startNode = nodes[startNodeIndex];

    curNode = startNode
    visited = []				#empty list of visited nodes to start
    visited.append(startNode)	
    unvisited = nodes[:]		#copy of entire node list
    del unvisited[startNodeIndex]	#remove the start node from the list of visited nodes

    #loop until unvisited list has only one node left
    while len(unvisited) > 1:
        node_1 = unvisited[0]
        node_2 = unvisited[1]
        node_1_index = 0
        node_2_index = 1
        minLocalPathDist = greedy_tsp.dist(curNode, node_1) + greedy_tsp.dist(node_1, node_2)
        
        for i in range(len(unvisited) - 1):
			for j in range(len(unvisited)):
				localPathDist = greedy_tsp.dist(curNode, unvisited[i]) + greedy_tsp.dist(unvisited[i], unvisited[j])
				if ((localPathDist < minLocalPathDist) and (i != j)):
					minLocalPathDist = localPathDist
					node_1 = unvisited[i]
					node_1_index = i

        curNode = node_1
        visited.append(node_1)
        del unvisited[node_1_index]

    visited.append(unvisited[0])		#visit the final node in the unvisited array
    visited.append(startNode)			#return to the starting point
    totalDist = greedy_tsp.pathDist(visited)		#calculate the total path distance

    return totalDist, visited			#return the total path distance and the path ordering

def greedyPeek2(nodes):
    """
    Description: Uses greedyPeek() to find a closest-neighbor path with look-ahead that visites each 
    node in an array of nodes exactly once.  Iterates through the list of nodes using each node as 
    a starting node, and determines which path yielded the minimum path distance.
    
    Input:
    nodes - an array of nodes in the form (unique identifier, x-coord, y-coord)
    
    Output: Returns the total path distance and an array of nodes in the order visited

    Time Complexity: O(n^4)
    """
    minResult = greedy_tsp.greedy(nodes)
    minPathDist = minResult[0]

    for i in range(len(nodes) - 1):
        result = greedyPeek(nodes, i)
        if result[0] < minPathDist:
            minResult = result
            minPathDist = result[0]

    return minResult


print("GREEDY_PEEK: ", greedyPeek(greedy_tsp.TEST_NODES))
greedy_tsp.printPathIdentifiers(greedyPeek(greedy_tsp.TEST_NODES)[1])
print
print("GREEDY_PEEK_2: ", greedyPeek2(greedy_tsp.TEST_NODES))
greedy_tsp.printPathIdentifiers(greedyPeek2(greedy_tsp.TEST_NODES)[1])
print