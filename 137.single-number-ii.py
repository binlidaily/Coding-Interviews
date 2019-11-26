#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        n = len(nums)
        for i in range(n):
            ones = (ones ^ nums[i]) & ~ twos
            twos = (twos ^ nums[i]) & ~ ones
        return ones
# 11/11 cases passed (60 ms)
# Your runtime beats 89.77 % of python3 submissions
# Your memory usage beats 53.33 % of python3 submissions (14.6 MB)
# @lc code=end

print(Solution().singleNumber([2,2,3,2]))
print(Solution().singleNumber([0,1,0,1,0,1,99]))