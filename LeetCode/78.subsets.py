#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, start, path, res):
        res.append(path)
        n = len(nums)
        for i in range(start, n):
            self.dfs(nums, i+1, path+[nums[i]], res)
# 10/10 cases passed (32 ms)
# Your runtime beats 91.37 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)

# 2. Iterative
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = [[]]
#         for n in nums:
#             l = len(res)
#             for i in range(l):
#                 res.append(res[i] + [n])
#         return res
# 10/10 cases passed (44 ms)
# Your runtime beats 35.69 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)

# 3. bit manipulation
class Solution3(object):
    def subsets(self, nums):
        res = []
        nums.sort()
        for i in range(1<<len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
# 10/10 cases passed (28 ms)
# Your runtime beats 97.24 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

