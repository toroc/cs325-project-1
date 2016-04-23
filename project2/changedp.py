
def changedp(coins, amount):

	maxw = amount + 1
	numCoins = len(coins)

	tUsed = [0 for x in range(maxw) ]
	tCount= [0 for x in range(maxw) ]
	
	# Store count of each coin value used
	minUsed = [0 for x in range(numCoins)]
	

	for p in range(amount+1):

		count = p
		nextCoin = 1


		for i in coins:
			if i <= p:
				if (tCount[ p - i] + 1 < count):
					count = tCount[p - i] + 1
					nextCoin = i 		
			else:
				break		

		tCount[p] = count
		tUsed[p] = nextCoin


	currVal = amount
	
	while currVal > 0:
		usedCoin = tUsed[currVal]
		# Parse thru the different coin values
		j = 0
		for coin in coins:
			if ( coin == usedCoin):
					minUsed[j] +=1
			j += 1

		currVal = currVal - usedCoin
		
		

	minCoinsAnswer = tCount[amount]

	return minUsed, minCoinsAnswer



# # Test the algo

# coins = [1, 2, 4, 8]
# value = 15

# answer = changedp(coins, value)
# print(answer)

	