fname = 'mbox-short.txt'
fhand = open(fname)
counts = dict()
for line in fhand:
	words = line.split()
	if not len(words) == 0 and words[0] == 'From' :
		start = words[1].find('@')
		domain = words[1][start+1:]
		if domain not in counts:
			counts[domain] = 1
		else:
			counts[domain] += 1
print(counts)
