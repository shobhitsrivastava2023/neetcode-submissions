class Solution:
    def jump(self, nums: List[int]) -> int:
        if (len(nums) == 1 and nums[0] != 0):
            return 0
        
        elif(len(nums) == 1 and nums[0] == 0):
            return 0

        farthest_reach  = 0
        min_steps = 0 
        current_index = 0 
        

        for i in range(len(nums)): 
            farthest_reach  = max(farthest_reach, i+ nums[i]) 
            if i == current_index: 
                min_steps += 1
                current_index = farthest_reach

            
            if current_index >= len(nums) - 1: 
                break 
        
        
        return min_steps
        
    

            



            
        