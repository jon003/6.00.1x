#!/usr/bin/python

def isPrime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  else: # not 1 and not an even number
    x = 2
    while x < n:
      if n % x == 0:
        return False
      x += 1
  return True


def primesList(N):
  '''
  N: an integer
  Returns a list of prime numbers
  '''
  primes = []
  for x in range(N+1):
    if isPrime(x):
      primes.append(x)

  return primes



print primesList(2)
