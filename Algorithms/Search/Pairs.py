#!/usr/bin/py
# Head ends here

# # timeout
# def pairs(a,k):
#     # a is the list of numbers and k is the difference value
#     a_sorted = sorted(a)
#     answer = 0
#     for i in range(len(a_sorted) - 1):
#         for j in range(i+1, len(a_sorted)):
#             if a_sorted[j] -  a_sorted[i] == k:
#                 answer += 1
#     return answer

def pairs(a,k):
    # a is the list of numbers and k is the difference value
    return len(set(a) & set(x + k for x in a))

if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))

