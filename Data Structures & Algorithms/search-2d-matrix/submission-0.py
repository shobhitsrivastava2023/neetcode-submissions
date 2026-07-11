class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) - 1
        while left <= right: 
            mid = left + (right -left)//2
            if target > matrix[mid][-1]: 
                left += 1 
            elif target < matrix[mid][0]: 
                right -= 1 
            else :
                break 
        
        if not left <= right: 
            return False 
        
        fetchedRow = left + (right - left)//2
        l = 0 
        r  = len(matrix[0]) - 1

        while l <= r: 
            m = l + (r - l)//2 
            if matrix[fetchedRow][m] < target: 
                l += 1
            elif matrix[fetchedRow][m] > target: 
                r -= 1
            elif matrix[fetchedRow][m] == target: 
                return True
        

        else: 
            return False

        