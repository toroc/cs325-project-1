#!usr/bin/env python

import sys
import processTestData

#test data input file is entered at the command line by the user when calling the program
#example:  python processData.py "testFileName.txt"
inputFilename = sys.argv[1]

processTestData.runAlgos(inputFilename)
