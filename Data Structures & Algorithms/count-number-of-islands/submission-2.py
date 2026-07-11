class Solution:
    def numIslands(self, grid):


        row = len(grid)
        col = len(grid[0])
        print(col)
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        count = 0

        def dfs(r,c): 
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0": 
                return 
            
            grid[r][c] = "0"
            
            for dr, dc in direction: 
                nr = r + dr
                nc = c + dc 
                dfs(nr, nc)
        
        for i in range(row): 
            for j in range(col): 
                if grid[i][j] == "1": 
                    count += 1 
                    dfs(i, j)
                    
                
        return count


        