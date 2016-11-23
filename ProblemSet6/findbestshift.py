'''
findbestshift function

takes: caesar encrypted text
returns: caesar shift of text that provides the most english words

pcode:
	take input text, strip punctuation
	for each possible shift, decode text
		split decoded text into words
			for each word you find in the dictionary, +1 the count

	return the shift with the highest count

'''

import string

def countWords(wordList, text):
	count = 0
	for word in text:
		if word in wordList:
			count += 1
	return count

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    bestkey = ''
    bestkeycount = 0

    text = text.translate(string.maketrans("",""), string.punctuation)
    for shift in range(26):
    	decoded = applyShift(text, shift)
    	count = countWords(wordList, decoded)
    	if count > bestkeycount:
    		bestkey = shift
    		bestkeycount = count

    return bestkey


