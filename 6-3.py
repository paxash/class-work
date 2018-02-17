def count(w, l):
	total = 0
	for letter in w:
		if letter in w:
			total = total + 1
		return total

word = input("Enter a word: ")
letter = input("Enter a letter: ")
answer = count(word, letter)
print(answer)
