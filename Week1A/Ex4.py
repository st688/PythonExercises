def sort_stack(stack):
	"""sort stack"""
	if not stack:
		return stack

	stack_tmp = list()
	# count how many items are there
	min_item = stack.pop()
	item_count = 0
	while True:
		if not stack:
			break
		if min_item > stack[-1]:
			stack_tmp.append(min_item)
			min_item = stack.pop()
		else:
			stack_tmp.append(stack.pop())
		item_count += 1

	stack.append(min_item)
	for i in range(item_count):
		stack.append(stack_tmp.pop())

	# keep finding the min item and put it back
	for i in range(item_count,1,-1):
		min_item = stack.pop()
		for j in range(i-1):
			if min_item > stack[-1]:
				stack_tmp.append(min_item)
				min_item = stack.pop()
			else:
				stack_tmp.append(stack.pop())
		stack.append(min_item)
		for j in range(i-1):
			stack.append(stack_tmp.pop())

	return stack

def ex4():
	print sort_stack([2,4,5,8,1,3])
	print sort_stack([7,6,5,4,3,2])
	print sort_stack([7,6,4,5,3,2])

if __name__ == "__main__":
	ex4()
