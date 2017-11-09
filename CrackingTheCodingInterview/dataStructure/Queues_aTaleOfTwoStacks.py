# python 3

class MyQueue(object):
    def __init__(self):
        self.myqueue = list()
    
    def peek(self):
        return self.myqueue[0]
        
    def pop(self):
        self.myqueue.pop(0)
        
    def put(self, value):
        self.myqueue.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = list(map(int, input().split()))
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        

