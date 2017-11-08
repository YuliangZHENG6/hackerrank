# python3
# bubble sort: O(n^2) time

def bubbleSort(arr, n):
    numSwaps = 0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                numSwaps += 1
        if numSwaps == 0:
            break
    return numSwaps, arr[0], arr[n-1]
             

n = int(input())
arr = list(map(int, input().strip().split(' ')))
numSwaps, firstEle, lastEle = bubbleSort(arr, n)
print("Array is sorted in %s swaps." % numSwaps)
print("First Element:", firstEle)
print("Last Element:", lastEle)

