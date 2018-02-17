fname = 'mbox-short.txt'
fhand = open(fname)
counts = dict()
for line in fhand:
	words = line.split()
	if not len(words) == 0 and words[0] == 'From' :
		counts[words[1]] = 1
print(counts)
