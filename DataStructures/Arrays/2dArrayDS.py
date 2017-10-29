#!/bin/python3

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

def sum_hourglass(r, c, arr):
    result = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
    return result
        
    
sum_max = -9*16
for r in range(4):
    for c in range(4):
        sum_temp = sum_hourglass(r, c, arr)
        sum_max = max(sum_temp, sum_max)
print(sum_max)

