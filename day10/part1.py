DEBUG = 0
FILE = "input.txt"
TEST = "test1"

TO_FIND = [20,60,100,140,180,220]

total = 0
sig = 1
cycles = 0
with open(TEST if DEBUG else FILE) as f:
	lines = f.readlines()

for line in lines:

	if "addx" in line:
		k = 2
		while k > 0:
			k -= 1
			cycles += 1
			if cycles in TO_FIND:
				total += sig * cycles
				print(cycles, sig, total)
		sig += int(line.split()[1])
	elif "noop" in line:
		cycles += 1
		if cycles in TO_FIND:
			total += sig * cycles
			print(cycles, sig, total)

print(total)
