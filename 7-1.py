fname = input("Enter the name of your file: ")
fhand = open(fname)
for line in fhand:
	sline = line.strip()
	print(sline.upper())

