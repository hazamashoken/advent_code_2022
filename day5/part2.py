from collections import defaultdict

with open("input.txt", "r") as f:
	lines = f.read().splitlines()

stacks = defaultdict(list)
for i, line in enumerate(lines):
	if (line.startswith(" ")):
		break
	for n, k in enumerate(line.split(), start=1):
		stacks[n].insert(0,k)
for key,val in stacks.items():
	stacks[key] = list(filter(lambda a: a != "[.]", stacks[key]))

for line in lines[i + 2:]:
	line = line.split()
	line.pop(0)
	line.pop(1)
	line.pop(2)
	many, f, t = map(int, line)
	ret = []
	while many != 0:
		many -= 1
		ret.insert(0,stacks[f].pop())
	stacks[t] += ret

for key, val in stacks.items():
	print(val.pop()[1], end="")
