'''
 Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.

 This function returns a list of all possible sublists in L of length n without skipping elements in L. 
 The sublists in the returned list should be ordered in the way they appear in L, 
  with those sublists starting from a smaller index being at the front of the list.

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list: 
[[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]
'''

def getSublists(L, n):
  sublists = []
  pos = 0
  while pos <= len(L) - n:
    sublists.append(L[pos:pos+n])
    pos += 1

  return sublists
    

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print getSublists(L,4)
print '[[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]'


L = [1, 1, 1, 1, 4]
print getSublists(L,2)
print '[[1, 1], [1, 1], [1, 1], [1, 4]]'
