#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = -1, n
        i = 0
        while i < r:
            if nums[i] == 0:
                l += 1
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
            elif nums[i] == 2:
                r -= 1
                nums[i], nums[r] = nums[r], nums[i]
            else:
                i += 1
        return nums
# 87/87 cases passed (32 ms)
# Your runtime beats 92.42 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# @lc code=end

