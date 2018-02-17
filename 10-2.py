fname = input('Enter a file name: ')
try:
	fhand = open(fname)
except:
	print('This file cannot be opened: ', fname)
	exit()
counts = dict()
for line in fhand:
	words = line.split()
	if not len(words) == 0 and words[0] == 'From' :
		d1, d2, d3 = words[5].split(':')
		if d1 not in counts:
			counts[d1] = 1
		else:
			counts[d1] += 1
lst = list()
for val, key in counts.items():
	lst.append((val, key))
lst.sort()
for key, val in lst :
	print(key, val)
