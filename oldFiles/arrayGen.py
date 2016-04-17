'''This program create files containing arrays of random numbers'''
import random

# To change the size of the array change the value of n
n = 45
# Open a file in write mode
fo = open("45.txt", "w+")
fo.write( "[" )
for i in range(n):
    x = random.randrange(-100, 100)
    x = str(x)
    fo.write( x )
    if i < n - 1:
        fo.write( ", " )
fo.write(  "]" )
# Close opend file
fo.close()