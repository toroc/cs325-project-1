
def changedp(coins, amount):

	maxw = amount + 1
	numCoins = len(coins)

	# Create two dimensional table
	minT = [[0 for x in range(maxw)]for y in range(numCoins)]
	
	# initialize the base case columns when coin value is 1

	for x in range(maxw):
		minT[0][x]= x

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
				# minimum between answer stored above OR 1 plus the answer for remaining sum
				minT[n][k] = min(minT[n-1][k], minT[n][nres]+1)
			else:
				minT[n][k] = minT[n-1][k]
			

	# print table
	# print(minT)
	
	minCoins = minT[numCoins-1][amount]
	# print(m)
	row = numCoins-1

	col = amount

	while col >= 0 and row >=0:
		prevCount = minT[row][col]
		checkCol = col - coins[row]
		curCount = minT[row][checkCol]

		if checkCol >=0 and curCount == prevCount - 1:		
			# used the coin
			minUsed[row] +=1
			# go to prev column
			col = col - coins[row]
		
		else:
			# go up a row
			row -= 1
	
	return minUsed, minCoins



	