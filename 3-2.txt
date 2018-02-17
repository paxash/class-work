try:
	hours = float(input('Number of Hours Worked: '))
	rate = float(input('Hourly Wage: '))
except:
	print("")
	print("Error, please enter numeric input")
	quit()
if hours > 40:
	pay = hours * rate + (hours - 40) * rate * 0.5
else:
	pay = hours * rate
print("")
print("Pay $", pay)
