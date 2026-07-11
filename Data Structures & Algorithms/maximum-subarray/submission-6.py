class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        sumN = 0
        largest_sum = float('-inf') 

        for num in nums: 
            if sumN < 0: 
                sumN = 0
            sumN += num
            largest_sum = max(largest_sum, sumN)
        
        return largest_sum

        