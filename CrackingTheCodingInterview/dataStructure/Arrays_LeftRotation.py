# python 3

def array_left_rotation(a, n, k):
    if n == 0:
        return a
    k = k % n     # flip rotation direction
    return a[k:] + a[:k]

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

