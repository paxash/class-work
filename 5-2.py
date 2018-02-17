biggest = None
smallest = None
while True:
	test = input('Enter a number: ')
	if test == "done" : break
	try:
		num = float(test)
	except:
		print("Invalid input")
		continue
	if smallest is None or num < smallest:
		smallest = num
	if biggest is None or num > biggest:
		biggest = num
print("Maximum: ", biggest)
print("Minimum: ", smallest)
