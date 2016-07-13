def same_elements_same_order(tuple1, tuple2):
	"""detect if two tuples have the same elements in the same order"""
	if len(tuple1) != len(tuple2):
		return False
	for i in range(len(tuple1)):
		if tuple1[i] != tuple2[i]:
			return False
	return True

def same_elements(tuple1, tuple2):
	"""detect if two tuples have the same elements"""
	tuple3 = list(tuple2)
	for i in range(len(tuple3)):
		tuple3[i] = False
	for item in tuple1:
		for i in range(len(tuple2)):
			if tuple2[i] == item and tuple3[i] == False:
				tuple3[i] = True
				break
	if False in tuple3:
		return False
	return True


def same_elements_ignore_duplicity(tuple1, tuple2):
	"""detect if two tuples have the same elements, ignoring duplicity"""
	for item in tuple1:
		if item not in tuple2:
			return False
	for item in tuple2:
		if item not in tuple1:
			return False
	return True

def ex1a():
	print "Do ('one', 'two', 'three') and ('one', 'two', 'three') have the same elements in the same order? "
	print same_elements_same_order(('one', 'two', 'three'), ('one', 'two', 'three'))
	print "Do ('one', 'two', 'three') and ('one', 'three', 'two') have the same elements in the same order? "
	print same_elements_same_order(('one', 'two', 'three'), ('one', 'three', 'two'))

	print "Do ('one', 'two', 'three') and ('one', 'three', 'two') have the same elements? "
	print same_elements(('one', 'two', 'three'), ('one', 'three', 'two'))
	print "Do ('one', 'two', 'three') and ('one', 'two', 'three', 'three') have the same elements? "
	print same_elements(('one', 'two', 'three'), ('one', 'two', 'three', 'three'))

	print "Do ('one', 'two', 'three') and ('two', 'one', 'three', 'three') have the same elements, ignoring duplicity? "
	print same_elements_ignore_duplicity(('one', 'two', 'three'), ('two', 'one', 'three', 'three'))
	print "Do ('one', 'two') and ('one', 'two', 'three') have the same elements, ignoring duplicity? "
	print same_elements_ignore_duplicity(('one', 'two'), ('one', 'two', 'three'))

if __name__ == "__main__":
	ex1a()
