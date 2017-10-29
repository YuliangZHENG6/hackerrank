n = int(input().strip())
arr=[int(x) for x in input().split(" ")]

left = []
right = []
equal = []
pivot = arr[0]
for e in arr:
    if e < pivot:
        left.append(e)
    elif e > pivot:
        right.append(e)
    elif e == pivot:
        equal.append(e)
result = left + equal + right
print(" ".join(map(str, result)))