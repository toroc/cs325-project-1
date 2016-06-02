# Takes as an argument the input file
#!usr/bin/env python
import sys
from greedy_tsp import greedy

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

inFile = sys.argv[1]

outFile = inFile + ".tour"
print outFile
cities, nodes = readCoords1(inFile)
cost, tour = greedy(nodes)
cost = str(cost)
cost = cost + "\n"
output = open(outFile, "w")
output.write(cost)
#print tour
count = 0
print len(tour)-1
for i in tour:
    out = str(i[0])
    out = out + "\n" 
    if (count != (len(tour)-1)):
        output.write(out)
    count = count + 1
output.close