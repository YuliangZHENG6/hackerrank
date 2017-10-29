#!/bin/python3

import sys

def isBalanced(s):
    # Complete this function
    table =  { ')': '(', ']':'[', '}':'{' }
    stack = []
    for x in s:
        if stack and table.get(x) == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    return "NO" if stack else "YES"
    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)

