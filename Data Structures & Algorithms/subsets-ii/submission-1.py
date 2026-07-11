class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        temp = [] 
        res = [] 
        nums.sort()

        def backtracking(i, temp): 
            if i  == len(nums): 
                res.append(temp[::])
                return 
            
            temp.append(nums[i])
            backtracking(i+1, temp)
            temp.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]: 
                i+= 1
            backtracking(i+1, temp)
            
        
        backtracking(0, [])
        return res
        