coins1 = [1, 5, 10, 25]

def changeSlow(coinList, val):
    m = 10000 # number of coins used
    c = [0 for k in range(len(coinList))] # denominations of coins
    firstList = [0 for k in range(len(coinList))]
    m, c = addDown(coinList, firstList, val, 0, m, c)
    #m, c = addDown(coinList, firstList, val, 0, m, c)
    return m, c
        
def addDown(coinList, oldList, val, i, m, c):
    newList = copyList(oldList)
    newList[i] += 1
    total = calcTotal(coinList, newList)
    if total == val:
        if sum(newList) < m:
            m = sum(newList)
            c = newList
        if i < len(newList)-1:
            newerList = copyList(newList)
            p = 0
            while p <= len(newList)-1:
                newerList[p] = 0
                p += 1
            m, c = addDown(coinList, newerList, val, i+1, m, c)
            newistList = copyList(newList)
            p = 1
            while p <= len(newList)-1:
                newistList[p] = 0
                p += 1
            m, c = addDown(coinList, newistList, val, i+1, m, c)
    if total < val:
        if i < len(coinList)-1:
            m, c = addDown(coinList, newList, val, i+1, m, c)
        m, c = addDown(coinList, newList, val, i, m, c)
    return m, c
    
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
        
changeSlow(coins1, 27)
