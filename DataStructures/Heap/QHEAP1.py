# python 3

from heapq import heappush, heappop
import sys

# By default: heapq is a min heap
# items: used to store the available elements in heap
heap = []
items = set()

def addElement(v):
    heappush(heap, v)
    items.add(v)
    
def deleteElement(v):
    items.discard(v)
    
def printMin():
    while heap[0] not in items:
        heappop(heap)
    print(heap[0])

n = int(input().strip())
for _ in range(n):
    query = input().strip().split(" ")
    if query[0] == "1":
        addElement(int(query[1]))
    elif query[0] == "2":
        deleteElement(int(query[1]))
    elif query[0] == "3":
        printMin()
    