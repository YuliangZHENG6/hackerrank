# python 3

N, Q = input().strip().split()
N, Q = int(N), int(Q)
lastAnswer = 0
S = [[] for i in range(N)]

for i in range(Q):
    sign, x, y = input().strip().split()
    x, y = int(x), int(y)
    index = ((x^lastAnswer)%N)
    if sign == "1":
        index = ((x^lastAnswer)%N)
        S[index].append(y)
    elif sign == "2":
        lastAnswer = S[index][y%len(S[index])]
        print(lastAnswer)
        
        