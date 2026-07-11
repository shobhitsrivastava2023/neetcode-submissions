class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        current_sum = 0
        max_sum = float('-inf')
        i = 0

        for i in range(len(nums)): 
            current_sum +=nums[i]
            max_sum = max(max_sum, current_sum)
            if current_sum < 0: 
                current_sum = 0
                
                
            
            
            
        
        return max_sum
            
        