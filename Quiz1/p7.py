def occurs(aDict, value):
  listdict = aDict.values()
  return listdict.count(value)

def uniqueValues(aDict):
  '''
  aDict: a dictionary
  '''
  # Your code here
  '''
  for each entry in the dict
    find how many times the value occurs in the dict.  
    if it occurs once, add to uniques dict.
  '''
  uniques = []
  for key in aDict:
    if occurs(aDict, aDict[key]) == 1:
      uniques.append(key)
  return uniques
