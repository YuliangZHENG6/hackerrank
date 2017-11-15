#!/bin/python3

import sys

def merge(arrL, arrR):
    swap, i, j, arrM, m, n = 0, 0, 0, [], len(arrL), len(arrR)
    ra = arrM.append
    while i < m and j < n:
        if arrL[i] <= arrR[j]:
            ra(arrL[i])
            i += 1
        else:
            ra(arrR[j])
            j += 1
            # count the inversion here
            swap += m - i
    arrM += arrL[i:]
    arrM += arrR[j:]    
    return arrM, swap

def mergeSort(arr):
    mid = len(arr) // 2
    if len(arr) > 1:
        arrL, swapL = mergeSort(arr[:mid])
        arrR, swapR = mergeSort(arr[mid:])
        arrM, swapM = merge(arrL, arrR)
        return arrM, int(swapL+swapR+swapM)
    else:
        return arr, 0
    

def countInversions(arr):
    # Complete this function
    arrM, swap = mergeSort(arr)
    return swap

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)


