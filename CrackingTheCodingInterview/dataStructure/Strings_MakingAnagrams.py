# python 3

"""
Using Counter
A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
"""

from collections import Counter

def number_needed(a, b):
    dict_a = Counter(a)
    dict_b = Counter(b)
    # find the difference 
    dict_a.subtract(dict_b)
    delete = sum(abs(i) for i in dict_a.values())      
    return delete

a = input().strip()
b = input().strip()

print(number_needed(a, b))

