size = int(input())
arr=[int(x) for x in input().split(" ")]
# arr = map(int, input().strip().split(" "))

def insertSort(arr, size):
    i = size - 1
    tmp = arr[i]
    while arr[i-1] > tmp and i > 0:
        arr[i] = arr[i-1]
        print (" ".join(map(str, arr)))
        i = i - 1
    arr[i] = tmp
    print(" ".join(map(str, arr)))
    return arr           
    
insertSort(arr, size)
