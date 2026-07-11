class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #  running two binary searches
        left = 0
        right = len(matrix) - 1
        mid  = 0

        while (left  <= right): 
            mid = left + (right - left)//2 
            if (matrix[mid][0] > target): 
                right = mid - 1
            elif (matrix[mid][-1] < target): 
                left = mid + 1
            
            else: 
                break
        
        if not (left <= right): 
            return False
        inLeft = 0 
        inRight = len(matrix[0]) - 1
        mid2 = 0

        while (inLeft <= inRight):
            mid2 = inLeft + (inRight - inLeft)//2 
            if (matrix[mid][mid2] > target):
                inRight = mid2 - 1

            
            elif (matrix[mid][mid2] < target): 
                
                inLeft = mid2 + 1
            elif (matrix[mid][mid2] == target): 
                return True
            
        return False
            

        


            

        