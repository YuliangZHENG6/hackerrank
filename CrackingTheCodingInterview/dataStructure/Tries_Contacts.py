# python 3

from collections import Counter

c = Counter()

def add(name):
    for i in range(1, len(name)+1):
        c[name[:i]]+=1
    
def find(partial):
    print(c[partial])

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if(op == 'add'):
        add(contact)
    else:
        find(contact)