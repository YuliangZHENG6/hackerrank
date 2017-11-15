# python 3

def bubbleSort(arr, n):
    swapNum = 0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapNum += 1
    return arr, swapNum

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
arr, swapNum = bubbleSort(arr, n)
print("Array is sorted in", swapNum, "swaps.")
print("First Element:", arr[0])
print("Last Element:", arr[-1])

