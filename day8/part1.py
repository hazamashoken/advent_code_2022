with open("input.txt", "r") as f:
	maps = f.read().splitlines()

height = len(maps)
length = len(maps[0])

maps = list(map(list, maps))
ret = [[maps[i][j] for i in range(len(maps))] for j in range(len(maps[0]))]

for i in range(height):
	row = []
	for j in range(length):
		try:
			if maps[i][j] > max(row):
				ret[i][j] = "X"
		except:
			ret[i][j] = "X"
		row.append(maps[i][j])

for j in range(length):
	row = []
	for i in range(height):
		try:
			if maps[i][j] > max(row):
				ret[i][j] = "X"
		except:
			ret[i][j] = "X"
		row.append(maps[i][j])

for i in range(height - 1, -1, -1):
	row = []
	for j in range(length - 1, -1, -1):
		try:
			if maps[i][j] > max(row):
				ret[i][j] = "X"
		except:
			ret[i][j] = "X"
		row.append(maps[i][j])

for j in range(length - 1, -1, -1):
	row = []
	for i in range(height - 1, -1, -1):
		try:
			if maps[i][j] > max(row):
				ret[i][j] = "X"
		except:
			ret[i][j] = "X"
		row.append(maps[i][j])
real = 0
for r in ret:
	real += r.count("X")

print(real)

