#!/bin/python3

import sys

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
# your code goes here
# method 1: too slow
#for ele in sorted([int(i) for i in unsorted]):
#    print(ele)
# method 2
for s in sorted(unsorted, key=int):
    print(s)
    

