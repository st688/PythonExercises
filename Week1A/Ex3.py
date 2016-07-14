def sum_reverse_order_linked_lists(list1,list2):
	if len(list1) > len(list2):
		list_out = list1 + [0]
		for i in range(len(list2)):
			digit_sum = list_out[i] + list2[i]
			list_out[i] = digit_sum % 10
			list_out[i+1] += int(digit_sum) / 10
	else:
		list_out = list2 + [0]
		for i in range(len(list1)):
			digit_sum = list_out[i] + list1[i]
			list_out[i] = digit_sum % 10
			list_out[i+1] += int(digit_sum) / 10
	if list_out[-1] == 0:
		list_out.pop()
	return list_out

def sum_forward_order_linked_lists(list1,list2):
	list1.reverse()
	list2.reverse()
	list_out = sum_reverse_order_linked_lists(list1,list2)
	list_out.reverse()
	return list_out

def ex3():
	print sum_reverse_order_linked_lists([7, 1, 6], [5, 9, 2])
	print sum_forward_order_linked_lists([6, 1, 7], [2, 9, 5])

if __name__ == "__main__":
	ex3()
