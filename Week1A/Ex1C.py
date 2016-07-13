def ex1c():
	"""find the 25 most frequently used words in The Complete Works of William Shakespeare"""
	dictionary = dict()
	with open('t8.shakespeare.txt', 'r') as fin:
		for line in fin:
			for word in line.split():
				if word in dictionary:
					dictionary[word] += 1
				else:
					dictionary[word] = 1
	sorted_dictionary = sorted(dictionary.iteritems(), key=lambda (k,v): (-v,k))

	for i in range(25):
		print sorted_dictionary[i][0]+" ",

if __name__ == "__main__":
	ex1c()
