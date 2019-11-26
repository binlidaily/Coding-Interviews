#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
from typing import List
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pivot = nums[0]
        n = len(nums)
        for i in range(1, n):
            pivot = pivot & nums[i]
        return pivot
# @lc code=end

print(Solution().singleNumber([2,2,3,2]))