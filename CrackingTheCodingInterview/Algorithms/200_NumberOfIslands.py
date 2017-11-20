# python 3

class Solution:
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.findIsland(grid, i, j)
                    num += 1
        return num
        
    def findIsland(self, grid, i, j): # DFS
        if (not(i in range(len(grid)) and j in range(len(grid[0])))):
            return 
        if grid[i][j] != "1":
            return 
        grid[i][j] = "#"                                           
        self.findIsland(grid, i-1, j)
        self.findIsland(grid, i+1, j)                                               
        self.findIsland(grid, i, j-1)
        self.findIsland(grid, i, j+1)                                      