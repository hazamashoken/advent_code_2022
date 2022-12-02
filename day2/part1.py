with open("input.txt", "r") as f:
	lines = f.read().splitlines()

total = 0

xyz = {
	'X': [1, 'C', 'A'],
	'Y': [2, 'A', 'B'],
	'Z': [3, 'B', 'C']
}

def check(l, r):
	if l in xyz[r]:
		return 6 if l == xyz[r][1] else 3
	return 0

for l in lines:
	f = l.split()
	total += xyz[f[1]][0]
	total += check(f[0], f[1])
	# print(total)
print(total)
