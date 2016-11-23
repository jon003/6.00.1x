

text = "Koala!!@ bears are soft and cuddly"
word = "koala"


text = text.lower()
print 'LOWER: %s' % text
print 'DEPUNC: %s' % text

if word in text.split():
  print 'hit: %s' % word
