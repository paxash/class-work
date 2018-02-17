def chop(c):
	del c[len(c)-1]
	del c[0]
	

colors = ['red', 'blue', 'green', 'yellow', 'purple']
chop(colors)
print(colors)
