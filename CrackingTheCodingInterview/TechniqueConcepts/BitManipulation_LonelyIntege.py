#!/bin/python3

import sys
from collections import Counter

def lonely_integer(a):
    c = Counter(a)
    for i in c:
        if c[i] == 1:
            return i
    return None

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

