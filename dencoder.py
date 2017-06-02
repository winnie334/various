alphabet = "abcdefghijklmnopqrstuvwxyz"
encodes = ['Encode', 'encode', 'e', 'E']
decodes = ['Decode', 'decode', 'd', 'D']

def clean(uncleantext):  # filters the text of characters that can't be ciphered
	for i in range(0, len(uncleantext)):
		for letter in uncleantext[i]:
			if letter not in alphabet:
				word = list(text[i])
				word.remove(letter)
				word = ''.join(word)
				uncleantext[i] = word
	return uncleantext

def shift(textlist):
	for i in range (0, len(textlist)):
		word = textlist[i]
		newword = ''
		shiftamount = len(word) # we will shift based on how long the word is
		for letter in word:
			pos = alphabet.index(letter)  # find what number the letter is
			if ed in encodes:
				newpos = (pos + shiftamount) % 26
			elif ed in decodes:
				newpos = (pos - shiftamount) % 26
			newword += alphabet[newpos]  # replace character with the one coming n after
		textlist[i] = newword + ' '
	return textlist


if __name__ == '__main__':
	ed = input('Encode or decode? (E/D) ')
	text = input("what's the text? ")
	text = text.lower().split()
	cleantext = clean(text)
	shifttext = shift(text)
	converted = ''.join(shifttext)
	print(converted)