#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        pivot = nums[0]
        for i in range(1, n):
            pivot = pivot ^ nums[i]
        return pivot
# 16/16 cases passed (80 ms)
# Your runtime beats 99.13 % of python3 submissions
# Your memory usage beats 9.84 % of python3 submissions (15.2 MB)

# @lc code=end

