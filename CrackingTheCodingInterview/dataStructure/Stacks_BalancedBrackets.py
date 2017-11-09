# python 3

def is_matched(expression):
    table = {"}": "{", "]": "[", ")": "("}
    stack = []
    for x in expression:
        if stack and table.get(x) == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    return False if stack else True
    

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

