# python3

N = int(input().strip())
di = {}
for i in range(N):
    s = input().strip()
    if s not in di:
        di[s] = 1
    else:
        di[s] += 1
        
Q = int(input().strip())
for i in range(Q):
    q = input().strip()
    if q in di:
        print(di[q])
    else:
        print(0)