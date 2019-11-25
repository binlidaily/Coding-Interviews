#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List
# @lc code=start
# Time: O(n^k)
# Space: O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        self.dfs(nums, 0, res)
        return res
    
    def dfs(self, nums, start, res):
        if not nums:
            return 
        n = len(nums)
        if start >= n:
            res.append(nums.copy())
            return
        
        for i in range(start, n):
            nums[start], nums[i] = nums[i], nums[start]
            self.dfs(nums, start+1, res)
            nums[start], nums[i] = nums[i], nums[start]
# 25/25 cases passed (36 ms)
# Your runtime beats 96.9 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
        
# @lc code=end

print(Solution().permute([1,2,3]))