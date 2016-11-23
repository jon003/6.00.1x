import string

def applyCoder(text, coder):
	"""
	Applies the coder to the text. Returns the encoded text.

	text: string
	coder: dict with mappings of characters to shifted characters
	returns: text after mapping coder chars to original text
	"""
	ciphertext = ''
	for letter in text:
		if letter in string.uppercase or letter in string.lowercase:
			ciphertext += coder[letter]
		else:
			ciphertext += letter

	return ciphertext    		




print applyCoder("Hello, world!", buildCoder(3))   # 'Khoor, zruog!'
print applyCoder("Khoor, zruog!", buildCoder(23))   # 'Hello, world!'
