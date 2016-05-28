#!usr/bin/env python
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



inputFilename = sys.argv[1]

file = open(inputFilename, "r")
nodes = readCoords(file)
#print(nodes)