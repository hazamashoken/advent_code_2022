file = open("input", "r")

number = file.read().splitlines()
lst = []
cur = 0
for i in number:
	if (i.isdigit()):
		cur += int(i)
	if not i.isdigit():
		lst.append(cur)
		cur = 0
print(max(lst))
print(sum(sorted(lst, reverse=True)[:3]))
