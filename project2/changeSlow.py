#coins1 = [1, 2, 4, 8, 16]
m = 10000 # number of coins used
c = [0 for k in range(len(coins1))] # denominations of coins

def changeSlow(coinList, val):
    firstList = [0 for k in range(len(coinList))]
    addDown(coinList, firstList, val, 0)
    addAccross(coinList, firstList, val, 0)
    print "Algorithm changeslow:"
    print c
    print m
    return m, c
        
def addDown(coinList, oldList, val, i):
    global m
    global c
    newList = copyList(oldList)
    newList[i] += 1
    total = calcTotal(coinList, newList)
    #print newList
    if total == val:
        if sum(newList) < m:
            m = sum(newList)
            c = newList
            #print "c=", newList, "m =", m
        if i < len(newList)-1:
            newerList = copyList(newList)
            p = 0
            while p <= len(newList)-1:
                newerList[p] = 0
                p += 1
            addAccross(coinList, newerList, val, i)
            newistList = copyList(newList)
            p = 1
            while p <= len(newList)-1:
                newistList[p] = 0
                p += 1
            addAccross(coinList, newistList, val, i)
    if total < val:
        addAccross(coinList, newList, val, i)
        addDown(coinList, newList, val, i)
    return 0
    
def addAccross(coinList, oldList, val, i):
    global m
    global c
    newList = copyList(oldList)
    if i < len(coinList)-1:
        i += 1
    newList[i] += 1
    #print newList
    total = calcTotal(coinList, newList)
    if total == val:
        if sum(newList) < m:
            m = sum(newList)
            c = newList
            #print "c=", newList, "m =", m
        
        if i < len(newList)-1:
            newerList = copyList(newList)
            p = 0
            while p <= len(newList)-1:
                newerList[p] = 0
                p += 1
            addAccross(coinList, newerList, val, i)
            newistList = copyList(newList)
            p = 1
            while p <= len(newList)-1:
                newistList[p] = 0
                p += 1
            addAccross(coinList, newistList, val, i)
    if total < val:
        addAccross(coinList, newList, val, i)
        addDown(coinList, newList, val, i)
    return 0
def calcTotal(coinList, list):
    totalValue = 0
    for i in range(len(coinList)):
        totalValue += coinList[i] * list[i]
    return totalValue

def copyList(oldList):
    newList = [0 for k in range(len(oldList))]
    for y in range(len(oldList)):
        newList[y] = oldList[y]
    return newList
        
#changeSlow(coins1, 120)