class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]          

        def line(lo, hi):           
            memo = {}
            def dfs(i):
                if i > hi:
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
                return memo[i]
            return dfs(lo)

        return max(line(0, n - 2), line(1, n - 1))