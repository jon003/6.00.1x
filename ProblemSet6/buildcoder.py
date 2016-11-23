
import string

def buildCoder(shift):
	"""
	Returns a dict that can apply a Caesar cipher to a letter.
	The cipher is defined by the shift value. Ignores non-letter characters
	like punctuation, numbers, and spaces.

	shift: 0 <= int < 26
	returns: dict
	"""
	caesar_dict = {}


	for i in range(26):
		offset = i + shift
		if offset > 25:
			offset -= 26
		caesar_dict.update({string.ascii_lowercase[i]:string.ascii_lowercase[offset]})
		caesar_dict.update({string.ascii_uppercase[i]:string.ascii_uppercase[offset]})

	return caesar_dict


print buildCoder(3)