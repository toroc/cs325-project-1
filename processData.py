

def insertIntoArrays():
    """
    Description: 
        Reads data from text file
        Converts each line in file into array of integers
        Appends next array to list of arrays
    Input: n/a 
    Output: Returns array of arrays (list of arrays)
    """

    arrayList = []

    with open('MSS_Problems.txt') as file:
        for line in file:
            #Get rid of brackets and empty space    
            line = line.replace('[', '').replace(' ', '').replace(']', '')

            #Append each number to list, add comma separator for next list
            arrayList.append([int(num) for num in line.split(',') if num not in '\n'])


    #print(arrayList)
    #print(arrayList[0]) 
    #print(arrayList[1])   
    
    return arrayList



#insertIntoArrays()





