#!/bin/python3

import sys

n = int(input().strip())
bi = bin(n)[2:]
result = max(bi.split('0')).count('1')
print(result)


