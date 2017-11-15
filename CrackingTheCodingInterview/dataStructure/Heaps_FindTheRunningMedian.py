#python3

"""
minheap: save items larger than the median, items
maxheap: save items smaller than the median, -items
"""

from heapq import heappush, heappop

n = int(input().strip())
minheap, maxheap = [], []
for _ in range(n):
    item = int(input().strip())
    if len(maxheap) > len(minheap):
        # now, maxheap[0] is the median
        if item < -maxheap[0]:
            heappush(minheap, -heappop(maxheap))
            heappush(maxheap, -item)
        else:
            heappush(minheap, item)
    elif len(minheap) > len(maxheap):
        # now, minheap[0] is the median
        if item > minheap[0]:
            heappush(maxheap, -heappop(minheap))
            heappush(minheap, item)
        else:
            heappush(maxheap, -item)
    else:
        if len(maxheap) == 0:
            heappush(maxheap, -item)
        else:
            if item > minheap[0]:
                heappush(maxheap, -heappop(minheap))
                heappush(minheap, item)
            else:
                heappush(maxheap, -item)
    if len(minheap) > len(maxheap):
        print("%.1f" % float(minheap[0]))
    elif len(maxheap) > len(minheap):
        print("%.1f" % float(-maxheap[0]))
    else:
        print("%.1f" % float(((-maxheap[0])+minheap[0])/2))
            
                     
        