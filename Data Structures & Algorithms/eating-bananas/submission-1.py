class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       # we might not need a helper function for this  

        left = 1
        right  = max(piles) 
        res = right 
        while(left <= right):
            mid  = left  + (right - left)//2
            totalTime  = 0 
            for p in piles: 
                totalTime  = totalTime  + math.ceil(float(p) / mid) 
            
            if totalTime <= h: 
                res = mid 
                right = mid - 1
            
            else: 
                left  = mid + 1
        
        return res


        


        