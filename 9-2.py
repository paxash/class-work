fname = 'mbox-short.txt'
fhand = open(fname)
counts = dict()
for line in fhand:
	words = line.split()
	if not len(words) == 0 and words[0] == 'From' :
		if words[2] not in counts:
			counts[words[2]] = 1
		else:
			counts[words[2]] += 1
print(counts)
