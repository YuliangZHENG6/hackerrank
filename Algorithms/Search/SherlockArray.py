#!/bin/python3

import sys

# Too Slow: timeout
#def solve(a):
#     # Complete this function
#     for i in range(len(a)):
#         if sum(a[:i]) == sum(a[i+1:]):
#             return "YES"
#     return "NO" 

def solve(a):
    # Complete this function
    sum = 0
    i = 0
    j = len(a)-1
    while(i != j):
        if(sum >=  0):
            sum -= a[j]
            j -= 1
        else:
            sum += a[i]
            i += 1
    if sum == 0:
        return "YES"
    else:
        return "NO"
    
T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)

