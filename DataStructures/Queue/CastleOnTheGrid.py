#!/bin/python3

import sys
from collections import deque

def minimumMoves(grid, startX, startY, goalX, goalY, n):
    # BFS 
    queue = deque()
    # queue element: (x, y, depth)
    queue.append((startX, startY, 0))
    visited = {}
   
    while queue:
        x, y, depth = queue.popleft()
        if x == goalX and y == goalY:
            print(depth)
            break
        else: 
            depth += 1
            ''' Need to break the traversal in two parts so that if we excounter X we can break the loop'''
            for i in range(x+1, n):
                if (i,y) not in visited:
                    if grid[i][y] == 'X':
                        break
                    else:
                        visited[(i,y)] = 1
                        queue.append((i,y,depth))
                else:
                    next
            for i in range(x-1, -1, -1):
                if (i,y) not in visited:
                    if grid[i][y] == 'X':
                        break
                    else:
                        visited[(i,y)] = 1
                        queue.append((i,y,depth))
                else:
                    next
            for i in range(y+1, n):
                if (x,i) not in visited:
                    if grid[x][i] == 'X':
                        break
                    else:
                        visited[(x,i)] = 1
                        queue.append((x,i,depth))
                else:
                    next
            for i in range(y-1, -1, -1):
                if (x,i) not in visited:
                    if grid[x][i] == 'X':
                        break
                    else:
                        visited[(x,i)] = 1
                        queue.append((x,i,depth))
                else:
                    next
        
    

if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid.append(input().strip())
    startX, startY, goalX, goalY = input().strip().split(' ')
    startX, startY, goalX, goalY = [int(startX), int(startY), int(goalX), int(goalY)]
    result = minimumMoves(grid, startX, startY, goalX, goalY, n)

