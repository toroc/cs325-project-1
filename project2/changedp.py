
def changedp(coins, amount):
	"""
	Description: Dynamic Programming algorithm to calculate the number of coins needed to make
	change for the given amount with the various values of coins at hand.
	
	Input:
	array coins - an array of the different possible denominations of coins
		Array of coins must be  in ascending order, with the first element value = 1
	int amount - the number of cents to make change for
	
	Output: an array in the form [numQuarters, numDimes, numNickels, numPennies] necessary
	to make change for the amount parameter

	O(nm): Iterates one time through the list of denominations but up to m times equal to the amount
	"""
	maxw = amount + 1
	
	numCoins = len(coins)

	# Create two dimensional table
	minT = [[0 for x in range(maxw)]for y in range(numCoins)]
	
	# initialize the base case columns when coin value is 1

	for x in range(maxw):
		minT[0][x] = x

	# print table
	minT[0][0] = 0
	# print(minT)
	# Store count of each coin value used
	minUsed = [0 for x in range(numCoins)]

	# Add min values at each column for each coin value row
	
	for n in range(1,numCoins):

		for k in range(maxw):

			if k >= coins[n]:
				nres = k - coins[n]
				# minimum between answer stored above OR 1 plus the answer for
				# remaining sum
				minT[n][k] = min(minT[n - 1][k], minT[n][nres] + 1)
			elif coins[n] > amount:
				break
			
					
	# print(m)
	row = numCoins - 1

	col = amount

	while col >= 0 and row >= 0:
		prevCount = minT[row][col]
		checkCol = col - coins[row]
		if checkCol >= 0:
			curCount = minT[row][checkCol]
			if curCount == prevCount - 1:
				# used the coin
				minUsed[row] +=1
				# go to prev column
				col = col - coins[row]
			else:
				# go up a row
				row -= 1
				
		else:
			row -=1
	# Save the num of coins used
	minCoins = 0
	for num in minUsed:
		minCoins += num
	
	return minCoins, minUsed



				
# coins = [1,6,13,37,150]
# amount = 126

# print(changedp(coins, amount))