# python 3


### method 1
# Without queue
n = int(input().strip())
arr = [[int(x) for x in input().split()] for _ in range(n)]

patrol = 0; pos=0
for i in range(n):
    patrol += (arr[i][0]-arr[i][1])
    if patrol < 0:
        pos = i+1
        patrol = 0

print(pos)


### method 2 
# A queue to save only proper elements

n = int(input().strip())
diff = []
for _ in range(n):
    petrol, dist = input().strip().split(" ")
    diff.append(int(petrol) - int(dist))
 
# count: number of elements in sum
# sum: sum of elements
# pos: starting index; the smallest index of the petrol pump from which we can start the tour
# i: the end index, in queue
count, pos, summ, i = 0, 0, 0, 0
while count != n:
    count += 1
    summ += diff[i] # inqueue
    while summ < 0:
        summ -= diff[pos] # dequeue
        pos += 1
        count -= 1
    i = (i+1)%n
print(pos)
    
    