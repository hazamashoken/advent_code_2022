with open("input.txt", "r") as f:
	lines = f.read().splitlines()

total = 0
print(ord('b') - (ord('a') - 1))
print(ord('A') - (ord('A') - 1))
for line in lines:
	l = line[:len(line) // 2]
	c = line[len(line) // 2:]
	let = set(c) & set(l)
	print(*let)
	total += ord(*let) - (ord('a') - 1) if list(let)[0].islower() else ord(*(set(c) & set(l))) - (ord('A') - 1) + 26
print(total)
