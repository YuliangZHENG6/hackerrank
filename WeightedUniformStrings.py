#!/bin/python3

import sys
import string

# build a dictionary (alphabet, weight)
di=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters]))

s = input().strip()
n = int(input().strip())

# compute possible weights
weights = set()
length = 1
for i in range(len(s)):
    weight = di[s[i]]
    length = length+1 if (i < len(s)-1 and s[i]==s[i+1]) else 1
    weights.add(weight*length)

# print results
for a0 in range(n):
    x = int(input().strip())
    print("Yes" if x in weights else "No")

