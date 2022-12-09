with open("input.txt", "r") as f:
	lines = f.read().splitlines()

SIZE = 0

# maps = []

# for i in range(SIZE):
	# maps.append(['.' for i in range(SIZE)])

# for n in maps:
# 	print("".join(n))

path = []
head = (SIZE//2, SIZE//2)
tails = [head[:] for i in range(9)]
print(tails)

def get_pos(y, x, yi, xi):
	if abs(y - yi) > 1 or abs(x - xi) > 1:
		if abs(y - yi) > 0:
			yi = yi + (y - yi)//abs(y - yi)
		else:
			yi = yi + (y - yi)
		if abs(x - xi) > 0:
			xi = xi + (x - xi)//abs(x - xi)
		else:
			xi = xi + (x - xi)
	return (yi, xi)

for line in lines:
	# print(line)
	c, m = line[0], int(line[1:])
	for i in range(m):
		if c == "U":
			head = (head[0] - 1, head[1])
		elif c == "D":
			head = (head[0] + 1, head[1])
		elif c == "L":
			head = (head[0], head[1] - 1)
		elif c == "R":
			head = (head[0], head[1] + 1)
		# path.append(head)
		print(tails)
		for n, tail in enumerate(tails):
			print(tail, n)
			if n == 0:
				tails[n] = get_pos(head[0], head[1], tails[n][0], tails[n][1])
			else:
				tails[n] = get_pos(tails[n-1][0], tails[n-1][1], tails[n][0], tails[n][1])
				# maps[tails[-1][0]][tails[-1][1]] = '#'
		# print("\nhead",head)
		# print("tail",tail)
		if tails[-1] not in path:
			path.append(tails[-1])
# for n in maps:
	# print("".join(n))
# print()
# for i in path:
# 	print(i)
print(len(path))

