
#!usr/bin/env python

import os

#import changeslow
import changegreedy
#import changedp

    

def insertIntoArrays(fileName):
    """
    Description: 
        Reads data from text file
        Converts each line in file into array of integers
        Appends next array to list of arrays
    Input: n/a 
    Output: Returns array of arrays (list of arrays)
    """

    arrayList = []

    with open(fileName) as file:
        for line in file:
            #Get rid of brackets and empty space    
            line = line.replace('[', '').replace(' ', '').replace(']', '')

            #Append each number to list, add comma separator for next list
            arrayList.append([int(num) for num in line.split(',') if num not in '\n'])
    
    return arrayList



def getOutputFilename(inputFilename):
    """
    Description:
        returns an output filename by first removing the file extension, and then
        appending the characters 'change.txt' to the end of the string
    Input: inputFilename - a string input filename
    Output: returns the modified string output filename
    """
    
    #use os to set the output filename based on the input filename
    return os.path.splitext(inputFilename)[0] + "change.txt"



def process(algo, algoName, inputFilename):
    """
    Description:
        Processes data from a .txt file by first reading each line of the input file into
        an array.  The format of the test data is such that the first line is an array
        of coin denominations and next line is a value to be attained using the given
        denominations.  The resulting array from reading the .txt file is:
        [[denominations], [value], [denominations], [value], ... , [denominations], [value]]

        The output filename is generated based on the name of the input file,
        and the solutions achieved by the given algorithm parameter are written to the output
        file on one line, and the total number of coins used are written on the next line.
    Input:
        algo - the algorithm used to calculate the number of coins needed of each denomination
        to achieve the total read from the input file

        algoName - a string descriptive name of the algorithm

        inputFilename - a string input filename
    Output:
        Generates a .txt file that is named based on the name of the input file.  Writes the
        solutions achieved by the given algorithm to the output file.  The format of the output
        file is:

        algoName
        [number of each denomination of coins]
        total number of coins needed
        ...
    """
    
    #convert each line from the input file into one element in the testData array
    #[[denominations], [amount], [denominations], [amount], ...]
    with open(inputFilename) as inputFile:
        testData = insertIntoArrays(inputFilename)

    #set the output filename using helper function
    outputFilename = getOutputFilename(inputFilename)
    outputFile = open(outputFilename, "a")
    outputFile.write("%s: \n" %algoName)

    #iterate over the pairs of testData, amount in the array
    for i in range(len(testData) // 2):
        result = algo(testData[2*i], testData[2*i + 1][0])
        writeResults(outputFile, result[1], result[0])

    outputFile.write("\n")



def writeResults(file, numEachCoin, totalCoins):
    """
    Description:
        Writes data to the given file
    Input:
        file - the file to write data to

        numEachCoin - an array

        totalCoins - an int
    Output:
        Writes a formatted array followed by a newline, and then writes an int followed by
        a newline.
    """
    
    file.write('{0}\n'.format(numEachCoin))
    file.write('{0}\n'.format(totalCoins))



def runAlgos(inputFilename):
    """
    Description:
        Runs each algorithm using the supplied input test file
        If the output filename already exists, all data is overwritten by the new results
    Input:
        inputFilename - a .txt file of test data
    Output:
        Creates an output file based on the name of the input file, and writes the results
        of each algorithm to the output file.
    """
    
    #clear the contents of the file if any exists
    open(getOutputFilename(inputFilename), "w").close()

    #write the new test data results to the file
    process(changegreedy.changegreedy, "changeslow", inputFilename) #change from changegreedy to changeslow
    process(changegreedy.changegreedy, "changegredy", inputFilename)
    process(changegreedy.changegreedy, "changedp", inputFilename)   #change from changegreedy to changedp

