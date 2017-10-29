n = int(input())
arrA = [int(x) for x in input().split(" ")]
m = int(input())
arrB = [int(x) for x in input().split(" ")]

l = max(arrA + arrB)
table = [0 for _ in range(l+1)]
for i in arrA:
    table[i] += 1
for i in arrB:
    table[i] -= 1

missing = [i for i in range(len(table)) if table[i] != 0]
print(" ".join(map(str, missing)))
    
    