#!/bin/python3

import sys

def leftRotation(a, d):
    # Complete this function
    b = a[(d%len(a)):]+ a[:(d%len(a))]
    return b

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))
    



