fname = 'mbox.txt'
fhand = open(fname)
counts = dict()
for line in fhand:
	words = line.split()
	if not len(words) == 0 and words[0] == 'From':
		counts[words[1]] = 1


lst = counts.keys()
for key in lst:
	if counts[key] == max(counts.values()):
		print(key, counts[key])
