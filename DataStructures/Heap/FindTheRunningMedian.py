# python 3

# method 1
from bisect import insort

def median(A):
    if len(A)%2==0:
        r = A[int(len(A)/2)]
        l = A[int(len(A)/2) - 1]
        med = float((l+r)/2.0)
    elif len(A)%2!=0:
        med = float(A[int(len(A)/2)])

    return med

A=[]
for _ in range(int(input())):
    insort(A,int(input()))
    med = median(A)
    print(med)



# method 2

"""
minheap: all elements > median
maxheap: all elements <= median
heapd: min heap
print:
    1. If minHeap.size()== maxHeap.size() median=(minHeap.top()+ maxHeap.top())/2; 
    2.Else If minHeap.size()>maxHeap.size() median=minHeap.top(); 
    3.Else median=maxHeap.top(); //for inserting first two elements, insert bigger element in minHeap and smaller in maxHeap. 
""" 

from heapq import heappush, heappop

minheap, maxheap = [], []
n = int(input().strip())
for _ in range(n):
    num = int(input().strip())
    if len(minheap) > len(maxheap):
        if num > minheap[0]:
            heappush(maxheap, -heappop(minheap))
            heappush(minheap, num)
        else: 
            heappush(maxheap, -num)
    elif len(maxheap) > len(minheap):
        if num < -maxheap[0]:
            heappush(minheap, -heappop(maxheap))
            heappush(maxheap, -num)
        else:
            heappush(minheap, num)
    else:
        if len(maxheap) == 0:
            heappush(maxheap, -num)
        else:
            if num > minheap[0]:
                heappush(maxheap, -heappop(minheap))
                heappush(minheap, num)
            else:
                heappush(maxheap, -num)
    if len(minheap) > len(maxheap):
        print("%.1f" % float(minheap[0]))
    elif len(maxheap) > len(minheap):
        print("%.1f" % float(-maxheap[0]))
    else:
        print("%.1f" % float(((-maxheap[0])+minheap[0])/2))
     
