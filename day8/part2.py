with open("input.txt", "r") as f:
	maps = f.read().splitlines()

height = len(maps)
length = len(maps[0])
maxt = 0

maps = list(map(list, maps))

# for i in range(height):
# 	for j in range(length):
# 		maps[i][j] = int(maps[i][j])

def check_top(cur, x ,y):
	if cur <= maps[y][x]:
		return 1
	if y > 0:
		return 1 + check_top(cur, x, y - 1)
	return 1

def check_buttom(cur, x ,y):
	if cur <= maps[y][x]:
		return 1
	if y < height - 1:
		return 1 + check_buttom(cur, x, y + 1)
	return 1

def check_left(cur, x ,y):
	if cur <= maps[y][x]:
		return 1
	if x < length - 1:
		return 1 + check_left(cur, x + 1, y)
	return 1

def check_right(cur, x ,y):
	if cur <= maps[y][x]:
		return 1
	if x > 0:
		return 1 + check_right(cur, x - 1, y)
	return 1

def check_visible(j , i):
	if i == 0 or j == 0 or i == height - 1 or j == length - 1:
		return 0
	t = check_top(maps[i][j], j, i - 1)
	b = check_buttom(maps[i][j], j, i + 1)
	l = check_left(maps[i][j], j + 1, i)
	r = check_right(maps[i][j], j - 1, i)
	return t * b * l * r


ret = []
for i in range(height):
	for j in range(length):
		ret.append(check_visible(j, i))
		print("i = {}, j = {}, ret = {}".format(i, j, ret[-1]))

# print(ret)
# c = 0
# for i in ret:
# 	print(i, end=" ")
# 	c+=1
# 	if c == len(maps[0]):
# 		print()
# 		c = 0
print(max(ret))
