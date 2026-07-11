class Solution:
    # brute force 

    # we appky the bfs until we find the zero and then we count the number of the iterations 
    # the moment we find zero we stop and then return the counted iteration 

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        
        
        def bfs(r,c): 
            q = deque([(r,c)])
           
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[r][c] = True
            steps = 0

            while q: 
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    
                    
                    for dr, dc in directions: 

                        nr, nc = row + dr, col + dc
                    

                        if 0 <= nr < ROWS and 0 <= nc < COLS and not visit[nr][nc] and grid[nr][nc] != -1:
                        
    
                            

                            q.append((nr, nc))
                            visit[nr][nc] = True;     
                steps += 1

                
            return INF 
        

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == INF: 
                    grid[r][c] = bfs(r,c)


            


        