fname = input("Enter the name of your file: ")
fhand = open(fname)
total = 0.0
count = 0
for line in fhand:
	if line.startswith("X-DSPAM-Confidence: ") :
		vline = float(line[20: ])
		total = total + vline
		count = count + 1
print("Spam Confidence Average: ", total/count)
