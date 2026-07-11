class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions  = ((0,1), (0,-1), (-1,0), (1,0))
        rows = len(board)
        cols = len(board[0])
        visited = set()
        
        def dfs(board, r,c, visited = None, i=0): 
            if visited == None:
                visited = set() 
            
            if r<0 or c<0 or r >= rows or c >= cols or (r,c) in visited or board[r][c] != word[i]:
                return False 
            visited.add((r,c))
            
            if i == len(word) - 1:
                return True

            for dr, dc in directions:
                if dfs(board, r+dr, c+dc, visited, i+1):
                    return True
            
            visited.remove((r,c))
                
        for r in range(len(board)): 
            for c in range(len(board[0])): 
                if dfs(board,r,c,visited,0):
                    return True 
        return False

        
        