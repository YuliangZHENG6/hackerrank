# python 3

"""
A comparison function is any callable that accept two arguments, compares them, and returns a negative number for less-than, zero for equality, or a positive number for greater-than. 
A key function is a callable that accepts one argument and returns another value to be used as the sort key.
"""


from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        pass 
    
    def comparator(a, b):
        diff = b.score - a.score
        if diff == 0:
            return -1 if a.name < b.name else 1
        return diff


# MAIN
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)