# python 3

'''
For each int i in the array A
    while stack is nonempty
        yield (i, top of stack)
        if i is less than the top of the stack, pop the stack
        otherwise break the while loop
    push i onto stack
'''

N = int(input().strip())
A = [int(x) for x in input().strip().split(" ")]

maxResult = A[0]^A[1]
stack = []
for x in A:
    while len(stack) != 0:
        if stack[len(stack)-1]^x > maxResult:
            maxResult = stack[len(stack)-1]^x
        if x < stack[len(stack)-1]:
            stack.pop()
        else:
            break
    stack.append(x)
print (maxResult)