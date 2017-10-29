n = int(input().strip())

for i in range(n):
    s = input().strip()
    # x[startAt:endBefore:skip]
    print(s[::2] + " " + s[1::2])

