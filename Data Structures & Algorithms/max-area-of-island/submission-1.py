class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS  = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        area = 0 
        count = 0 
        def dfs(r,c): 
            nonlocal area 
            nonlocal count
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0: 
                return 
            grid[r][c] = 0
            count += 1
            for dr, dc in directions: 
                nr = r + dr 
                nc = c + dc
                dfs(nr,nc) 
                area = max(area, count)
                
        
        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                if grid[r][c] == 1: 
                    dfs(r,c)
                    count = 0
        return area

            

        