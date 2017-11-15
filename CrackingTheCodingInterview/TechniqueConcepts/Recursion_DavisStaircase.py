# python 3

# # Time Out
# def ways(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3: 
#         return 4
#     else:
#         return ways(n-1) + ways(n-2) + ways(n-3)



memory = {1:1, 2:2, 3:4}
def ways(n):
    if not n in memory.keys():
        memory[n] = ways(n-1) + ways(n-2) + ways(n-3)
    return memory[n] 
        
s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(ways(n))

