def string_compression(string):
	if len(string) == 0:	# empty string
		return string

	char = string[0]
	num  = 1

	string_out = char

	for i in range(1,len(string)):
		if char != string[i]:
			string_out += (str(num) + string[i])
			num  = 1
			char = string[i]
		else:
			num += 1
	string_out += str(num)

	if len(string_out) < len(string):
		return string_out
	else:
		return string

def ex2b():

	print string_compression("aabcccccaaa")
	print string_compression("abc")

if __name__ == "__main__":
	ex2b()
