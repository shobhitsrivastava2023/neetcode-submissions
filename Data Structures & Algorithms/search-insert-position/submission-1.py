class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 
        countIndex = len(nums)

        while (left <= right): 
            mid  = left + (right - left)//2
            if( nums[mid] == target): 
                return mid 
            if (nums[mid] < target): 
                countIndex = mid
                left = mid+1 
            else: 
                right = mid - 1
            
        return left