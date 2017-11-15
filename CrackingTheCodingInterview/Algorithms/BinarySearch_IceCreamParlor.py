# python 3

def get_flavours(money,flavours):
    map = {}
    for pos, cost in enumerate(flavours):
        if cost in map:
            return (map[cost], pos + 1)
        else:
            map[money-cost] = pos + 1

t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    pos0, pos1 = get_flavours(m, a)
    print(pos0, pos1)

