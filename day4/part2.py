with open("input.txt", "r") as f:
	lines = f.read().splitlines()
total = 0

for line in lines:
	l, r = line.split(",")
	l = list(map(int, l.split("-")))
	r = list(map(int, r.split("-")))
	l = set(range(l[0], l[1] + 1))
	r = set(range(r[0], r[1] + 1))
	if l & r or r & l:
		total += 1
print(total)
