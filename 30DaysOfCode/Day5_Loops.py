#!/bin/python3

import sys

n = int(input().strip())
print('\n'.join('%d x %d = %d'%(n, i, n*i) for i in range(1, 11)))

