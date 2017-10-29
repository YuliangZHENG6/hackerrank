size = int(input())
arr=[int(x) for x in input().split(" ")]

def insert(arr):
    i = len(arr) - 1
    tmp = arr[i]
    while arr[i-1] > tmp and i > 0:
        arr[i] = arr[i-1]
        i = i - 1
    arr[i] = tmp
    return arr

def insertSort(arr, size):
    sort = []
    for i in range(2,size+1):
        sort = insert(arr[:i])
        arr = sort + arr[i:]
        print(" ".join(map(str, arr)))
        
insertSort(arr, size)
        
    