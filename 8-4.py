fname = input('Enter your file name: ')
fhandle = open(fname)
answer = []
for line in fhandle:
	nlist = line.split()
	for x in nlist:
		if x in answer: continue
		answer.append(x)
answer.sort()
print(answer)
