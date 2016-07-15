from collections import deque

def ex5():
	d = deque()
	d.append(1)
	d.extend([6,7,8])
	d.append(2)
	d.rotate(1)
	d.append(len(d))
	d.extendleft([0])
	d.pop()
	d.popleft()
	d.rotate(-2)

	print d

if __name__ == "__main__":
	ex5()
