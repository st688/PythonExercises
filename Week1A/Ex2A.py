def string_permulation_detector(string1,string2):
	"""string permutation detector"""
	return ''.join(sorted(string1)) == ''.join(sorted(string2))

def ex2a():
	print string_permulation_detector("I saw elba","able was I")
	print string_permulation_detector("this is not","permulation")

if __name__ == "__main__":
	ex2a()
