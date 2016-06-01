# Takes as an argument the input file

import sys
from tspSimulated import readCoords1, tspSimulated2

inFile = sys.argv[1]

outFile = inFile + ".tour"
print outFile
cities, nodes = readCoords1(inFile)
cost, tour = tspSimulated2(cities, nodes)
cost = str(cost)
cost = cost + "\n"
#tour = str(tour)
output = open(outFile, "w")
output.write(cost)
for i in tour:
    out = str(tour[i])
    out = out + "\n"
    output.write(out)
output.close