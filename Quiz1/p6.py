def count7(N):
    '''
    N: a non-negative integer
    Must be recursive.
    '''
    # Your code here

    if N == 7:
      return 1
    if N < 10 and N != 7:
      return 0
    elif N % 10 == 7:
      return count7(N / 10) + 1
    else:
      return count7(N / 10) 

print count7(717)
print count7(1237123)
print count7(8989)

