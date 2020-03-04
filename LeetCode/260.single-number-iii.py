#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        code = 0
        for num in nums:
            code ^= num
        code &= -code # get contain last 1 number
        a, b = 0, 0
        for num in nums:
            if num & code != 0:
                a ^= num
            else:
                b ^= num
        return [a, b]
# Runtime: 72 ms, faster than 11.80%
# Memory Usage: 14.4 MB, less than 100.00% 

# @lc code=end

