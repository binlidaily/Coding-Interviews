#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_num = set(nums)
        if len(nums) > len(set_num):
            return True
        else:
            return False

# 18/18 cases passed (128 ms)
# Your runtime beats 67.09 % of python3 submissions
# Your memory usage beats 88.68 % of python3 submissions (18.1 MB)
# @lc code=end

print(Solution().containsDuplicate([1,2,3,1]))  # True
print(Solution().containsDuplicate([1,2,3,4]))  # False
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # True