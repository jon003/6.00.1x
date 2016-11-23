

'''
 Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.

 This function returns a list of all possible sublists in L of length n without skipping elements in L. 
 The sublists in the returned list should be ordered in the way they appear in L, 
  with those sublists starting from a smaller index being at the front of the list.
'''

def getSublists(L, n):
  sublists = []
  pos = 0
  while pos <= len(L) - n:
    sublists.append(L[pos:pos+n])
    pos += 1

  return sublists

def check_sequence(L):
  for i in range(len(L) - 1):
    print 'Checking %d is less than or equal to %d.' % (L[i], L[i+1])
    if L[i] > L[i+1]:
      return False
  return True

def getAllSublists(L):
  ''' make a list of all of the possible sublists of L in descending length order. '''
  allsublist = []
  length = len(L)
  while length > 0:
    allsublist.append(getSublists(L,length))
    length -= 1
  return allsublist


L1 = '[5, 7, 7, 2]'
print getAllSublists(L1)
   

def longestRun(L) :
  biglist = getAllSublists(L)
  for sublist in biglist:
    if check_sequence(sublist):
      return sublist
  
