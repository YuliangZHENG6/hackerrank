#!/bin/python3

import sys
from collections import Counter

def sherlockAndAnagrams(s):
    di = dict()
    for i in range(len(s)):
        for j in range(len(s) - i):
            # using the frozenset to have immutable set
            # the dictionary now has keys: a set show the appeared alphabet and alphabet's occurrences.
            # e,g. ((('a', 1), ('b', 2)), 2)
            # a possible string with one 'a' and two 'b', occurs 2 times of different arrangement
            key = frozenset(Counter(s[i:j+1+i]).items()) # O(N) time key extract
            di[key] = di.get(key, 0) + 1
    count = 0
    for key in di:
        count += (di[key] - 1)*di[key]//2
    return count

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)

