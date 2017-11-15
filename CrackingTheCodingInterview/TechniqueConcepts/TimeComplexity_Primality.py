# python 3

"""
Suppose one number is a factor of N and that it is smaller than the square-root of the number N. Then the second factor must be larger than the square-root.
"""

from math import sqrt 

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)+1)):
            if n%i == 0:
                return False
        return True
    else:
        return False

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")