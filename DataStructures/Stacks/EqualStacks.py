#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

# reverse to make the top at the top of stack
h1.reverse()
h2.reverse()
h3.reverse()

listStacks = [h1, h2, h3]
listSum = [sum(h1), sum(h2), sum(h3)]

while((listSum[0] != listSum[1]) or listSum[1] != listSum[2]):
    # if not equal delete one element from the stack with max sum
    a = listStacks[listSum.index(max(listSum))].pop()
    listSum[listSum.index(max(listSum))] -= a
print (listSum[0])



