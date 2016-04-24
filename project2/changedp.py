
def changedp(coins, amount):

	maxw = amount + 1
	numCoins = len(coins)

	# Create two dimensional table
	minT = [[0 for x in range(maxw)]for y in range(numCoins)]
	
	# initialize the base case columns when coin value is 1
	for x in range(maxw):
		minT[0][x]= x

	# print table
	print(minT)
	# Store count of each coin value used
	minUsed = [0 for x in range(numCoins)]

	# Add min values at each column for each coin value row
	for n in range(1,numCoins):
		for k in range(maxw):

			if k >= coins[n]:
				# minimum between answer stored above OR 1 plus the answer for remaining sum
				minT[n][k] = min(minT[n-1][k], minT[n][k-coins[n]]+1)
			else:
				minT[n][k] = minT[n-1][k]
			

	# print table
	print(minT)
	
	m = minT[numCoins-1][amount]
	# print(m)
	row = numCoins-1

	col = amount

	while col >= 0:
		if row == 0:
			# move left to previous col
			col -= coins[col]
			# minUsed[row] += 1
		elif minT[row-1][col] >= minT[row][col - coins[row]]+1:
			# move left to prev col
			col -= coins[row]
			minUsed[row] +=1
		else:
			# Go up a row
			row -= 1


	return minUsed, m

# Test the algo

coins = [1, 3, 7, 12]
value = 29

answer = changedp(coins, value)

print(answer)
	