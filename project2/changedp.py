
INF = 1000000

def changedp(coins, amount):

	maxw = amount + 1
	numCoins = len(coins)

	coinUsedTable = [0 for x in range(maxw) ]
	coinCountTable = [0 for x in range(maxw)]

	# Store 
	coinsUsed = [0 for x in range(maxw)]
	
	# Store solution
	minCoinsUsed = [0 for x in range(numCoins)]


	for p in range(amount+1):

		coinCount = p
		nextCoin = 1


		for i in [coinValue  for coinValue in coins if coinValue <= p]:
			if (coinCountTable[ p - i] + 1 < coinCount):
				coinCount = coinCountTable[p - i] + 1
				nextCoin = i 

		coinCountTable[p] = coinCount
		coinUsedTable[p] = nextCoin

	###################################Up to here the above works correctly #########################

	currVal = amount
	# Should do this for each coin value


	while currVal > 0:
		usedCoin = coinUsedTable[currVal]
		# Parse thru the different coin values
		j = 0
		for coin in coins:
			if ( coin == usedCoin):
				minCoinsUsed[j] +=1
			j += 1

		currVal = currVal - usedCoin
		
		

	minCoinsAnswer = coinCountTable[amount]

	return minCoinsUsed, minCoinsAnswer



# Test the algo

coins = [1, 3, 7, 12]
value = 29

print(changedp(coins, value))

	