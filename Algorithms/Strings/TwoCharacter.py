#!/bin/python3

import sys

s_len = int(input().strip())
s = input().strip()

st = list(set(s))

def validateT(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return False
    return True

length = 0
for i in range(len(st)):
    for j in range(i+1, len(st)):
        string = [c for c in s if c==st[i] or c==st[j]]
        if validateT(string):
            length = max(len(string), length)
         
print(length)

    

