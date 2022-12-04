with open("input.txt", "r") as f:
	lines = f.read().splitlines()

total = 0

for n in range(len(lines)):
	if n % 3 == 0:
		let = set(lines[n]) & set(lines[n + 1]) & set(lines[n + 2])
		print(*let)
		total += ord(*let) - (ord('a') - 1) if list(let)[0].islower() else ord(*let) - (ord('A') - 1) + 26
print(total)
