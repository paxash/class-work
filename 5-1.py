count = 0
total = 0
while True:
	test = input('Enter a number: ')
	if test == "done" :
		break
	try:
		num = float(test)
	except:
		print("Invalid input")
		continue
	count = count + 1
	total = total + num
print("")
print("Total: ", total)
print("Count: ", count)
print("Average: ", total/count)
