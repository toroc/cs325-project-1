


def changedp(coins, amount):

	MAXW = amount + 1
	minCoins = [0 for x in range(MAXW) ]
	coinsUsed = [0 for x in range(MAXW)]
	prevSub = [0 for x in range(MAXW)]
	lastItem = [ 0 for x in range(MAXW)]
	solution = list()


	coinCount = 0

	# DP Base: fill entries for case when amount = 0

	for centVal in range(amount + 1):

		coinCount = centVal
		nextCoin = 1

		for j in [w for w in coins if w <= centVal]:
			if minCoins[centVal - j ] + 1 < coinCount:
				coinCount = minCoins[centVal - j] + 1
				nextCoin = j
		minCoins[centVal] = coinCount
		coinsUsed[centVal] = nextCoin

	# Complete the other table entries at each sub

	currVal = amount

	while currVal > 0:
		usedCoin = coinsUsed[currVal]
		solution.append(usedCoin)
		currVal = currVal - usedCoin

	minCoinsAnswer = minCoins[amount]

	return solution, minCoinsAnswer



# Test the algo

coins = [1, 3, 7, 12]
value = 29

print(changedp(coins, value))

	