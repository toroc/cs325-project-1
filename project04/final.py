#!/usr/bin/python
# Takes as an argument the input file

import sys
from tspSimulated import readCoords1, tspSimulated, tspSimulated2

inFile = sys.argv[1]

outFile = inFile + ".tour"
print outFile
cities, nodes = readCoords1(inFile)
if (len(nodes) < 1000):
    cost, tour = tspSimulated(cities, nodes)
else:
    cost, tour = tspSimulated2(cities, nodes)
cost = str(cost)
cost = cost + "\n"
#tour = str(tour)
output = open(outFile, "w")
output.write(cost)
for i in tour:
	#print(i)
	#print(tour[i])
    out = str(i)
    out = out + "\n"
    output.write(out)
output.close