DEBUG = 0
FILE = "input.txt"
TEST = "test1"

TO_FIND = [40,80,120,160,200,240]
img = []
cur = ["."]
sig = 1
cycles = 0

with open(TEST if DEBUG else FILE) as f:
	lines = f.readlines()

def sprite_pos(pos):
	buffer = ["." for i in range(40)]
	for i in range(3):
		if pos + i < 40:
			buffer[pos + i] = "#"
	return buffer

sp = sprite_pos(0)

for line in lines:
	if "addx" in line:
		for _ in range(2):
			cycles += 1
			if cycles in TO_FIND:
				img.append(cur)
				cur = []
			cur.append(sp[cycles % 40])
		sig += int(line.split()[1])
	elif "noop" in line:
		cycles += 1
		if cycles in TO_FIND:
			img.append(cur)
			cur = []
		cur.append(sp[cycles % 40])
	sp = sprite_pos(sig)




for m in img:
	print("".join(m))
