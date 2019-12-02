#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         if not nums:
#             return []
#         nums.sort()
#         res = []
#         self.dfs(nums, 0, [], res)
#         return res

#     def dfs(self, nums, start, path, res):
#         res.append(path)
#         n = len(nums)
#         for i in range(start, n):
#             if i > start and nums[i-1] == nums[i]:
#                 continue
#             self.dfs(nums, i+1, path+[nums[i]], res)
# 19/19 cases passed (44 ms)
# Your runtime beats 64.04 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)

# 2. Iterative
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # there is a more concise version
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res) # magic l !!!!
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res
# 19/19 cases passed (44 ms)
# Your runtime beats 64.04 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13 MB)
# @lc code=end

print(Solution().subsetsWithDup([1,2,2]))