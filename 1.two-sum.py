#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
import collections
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = collections.defaultdict()
        n = len(nums)
        for i in range(n):
            if target - nums[i] in hash_table:
                return [i, hash_table[target - nums[i]]]
            else:
                hash_table[nums[i]] = i
        return [-1, -1]
# @lc code=end

