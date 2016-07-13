from random import randint

def rotate90(matrix):
	"""rotate the input matrix by 90 degrees (counterclockwise) in place"""
	n = len(matrix)
	i = 0		# row index
	for i in range(n):
		for j in range(i,n-i-1):
			tmp = matrix[i][j]
			matrix[i][j]     = matrix[j][n-i-1]
			matrix[j][n-i-1] = matrix[n-i-1][n-j-1]
			matrix[n-i-1][n-j-1] = matrix[n-j-1][i]
			matrix[n-j-1][i] = tmp

	return matrix

def ex1b():
	# Create a list containing 2 lists, each of 2 items, all set to 0
	w, h = 2, 2
	Matrix = [[0 for x in range(w)] for y in range(h)]
	# Use random assignment to create the image for rotation
	Matrix[0][0] = randint(0,1)
	Matrix[0][1] = randint(0,1)
	Matrix[1][0] = randint(0,1)
	Matrix[1][1] = randint(0,1)

	print "input:"
	for row in Matrix:
		for val in row:
			print '{:4}'.format(val),
		print

	Matrix_out = rotate90(Matrix)
	print "output:"
	for row in Matrix_out:
		for val in row:
			print '{:4}'.format(val),
		print

	##########
	w, h = 5, 5
	Matrix = [[0 for x in range(w)] for y in range(h)]
	for i in range(h):
		for j in range(w):
			Matrix[i][j] = randint(0,1)

	print "input:"
	for row in Matrix:
		for val in row:
			print '{:4}'.format(val),
		print

	Matrix_out = rotate90(Matrix)
	print "output:"
	for row in Matrix_out:
		for val in row:
			print '{:4}'.format(val),
		print	


if __name__ == "__main__":
	ex1b()
