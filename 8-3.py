fname = 'mbox-short.txt'
try:
	fhand = open(fname)
except:
	print('This file could not be found: ', fname)
	quit()
try:
	for line in fhand:
		words = line.split()
		if not len(words) == 0 and words[0] == 'From' : print(words[2])
except:
	print('This file: ', fname, 'has no data available.')
	quit()
