with open("input.txt", "r") as f:
	line = f.readline()

ret = []

for n, i in enumerate(line, start=1):
	ret.append(i)
	if len(ret) > 4:
		ret.pop(0)
	print(ret, i)
	if len(set(ret)) == 4:
		break
print(n)
