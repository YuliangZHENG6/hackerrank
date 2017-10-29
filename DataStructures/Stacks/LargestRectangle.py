#!/bin/python3

import sys


"""
Idea: to check left and right side, count the possible buildings to form rectangle
"""

# NEVER use stack at all

def largestRectangle(n, h):
    # Complete this function
    largest = 0
    for i in range(n):
        count = 1
        for left in range(i-1, -1, -1):
            if h[left] >= h[i]:
                count += 1
            else:
                break
        for right in range(i+1, n):
            if h[right] >= h[i]:
                count += 1
            else:
                break
        largest = max(largest, h[i]*count)
    return largest
    

if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    result = largestRectangle(n, h)
    print(result)


