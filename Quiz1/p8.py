def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """

    iterList = list(L)
    for s in iterList:
      if not f(s):
        L.remove(s)
    return len(L)    


def f(s):
    return 'a' in s

'''
def f(s):
    if len(s) > 2:
	    return True 
    else:
      return False

def f(s):
	if s:
		return True
	else:
		return False
'''      
L = ['a', 'b', 'a', 'zzz', 'abcdefghijklmnopqrtuzwxyz', '', '9', '\\']

print satisfiesF(L)
print L




# this will then be called with:
#run_satisfiesF(L, satisfiesF)
