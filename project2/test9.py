#!usr/bin/env python

import changedp
import changegreedy

DENOMINATIONS = [1,3,9,27]

def part9():
    """
    Description: Used to test the range of values for part 9 in project 2
    Prints the results of changedp and changegreedy for every value in the
    range (9,37)
    """
    for i in range(9,37):
        print("changedp")
        print(changedp.changedp(DENOMINATIONS, i))
        print("changegreedy")
        print(changegreedy.changegreedy(DENOMINATIONS, i))
        print("#######################################################")
