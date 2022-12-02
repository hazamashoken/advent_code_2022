with open("input.txt", "r") as f:
	lines = f.read().splitlines()
'''
X = 1 rock            A = rock paper 2
Y = 2 paper            B = paper sicssors 3
Z = 3 scissors        C = scissors rock 1

win = 6
lose = 0
draw = 3
'''
cond = {
	'Z': {
		'A': 6 + 2,
		'B': 6 + 3,
		'C': 6 + 1
	},
	'Y': {
		'A': 3 + 1,
		'B': 3 + 2,
		'C': 3 + 3
	},
	'X': {
		'A': 0 + 3,
		'B': 0 + 1,
		'C': 0 + 2
	}
}

total = 0

for line in lines:
	l,c = line.split()
	total += cond[c][l]
print(total)

