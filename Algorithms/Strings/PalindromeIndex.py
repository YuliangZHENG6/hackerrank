#!/bin/python3
# time complexity: O(N)
# space complexity: O(N)

import sys

def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

#def isPalindrome(s):
#    for idx in range(len(s)//2):
#        if s[idx] != s[len(s)-idx-1]:
#            return False
#    return True
 
def palindromeIndex(s):
    for i in range((len(s)+1)//2):
        if s[i] != s[len(s)-i-1]:
            if isPalindrome(s[:i]+s[i+1:]):
                return i
            else:
                return len(s)-i-1
    return -1
            

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)

