fname = input("Enter the name of your file: ")
count = 0
try:
	fhand = open(fname)
except: 
	if fname.upper() == "NA NA BOO BOO":
		print("NA NA BOO BOO TO YOU - You have been punk'd!")
	else:
		print("This file can't be opened: ", fname)
		quit()
for line in fhand:
	if line.startswith('Subject: ') :
		count = count + 1
print("There were "+str(count)+" subject lines in "+fname)
