def GenerateMagicSquare(n):
#initializing the array
	magic = [[0 for x in range(n)]
				for y in range(n)]
	#setting row and column value
	i = n // 2
	j = n - 1
	k = 1
	while k <= (n * n):
	    #checking condition (c)
		if i == -1 and j == n: 
			j = n - 2
			i = 0
		else:
			#checking condition (a)
			if j == n:
				j = 0
			if i < 0:
				i = n - 1
        #checking conditon (b)
		if magic[i][j]: 
			j = j - 2
			i = i + 1
			continue
		else:
		    #placing the number into the array
			magic[i][j] = k
			k = k + 1
        #for the next number setting (i-1, j+1)
		j = j + 1
		i = i - 1 
	#printing the matrix
	for i in range(0, n):
		for j in range(0, n):
			print('%2d ' % (magic[i][j]),end='')
			if j == n - 1:
				print()
#This code works for only odd numbers
n = 7
print("The magic sum is ",n * (n * n + 1) // 2, "\n")
GenerateMagicSquare(n)