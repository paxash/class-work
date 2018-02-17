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
		if words[1] not in counts:
			counts[words[1]] = 1
		else:
			counts[words[1]] += 1
lst = list()
for key, val in counts.items():
	lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst[:3] :
	print(key, val)
