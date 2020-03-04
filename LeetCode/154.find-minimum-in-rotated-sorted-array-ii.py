#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
from typing import List
# @lc code=start
# O(logn)
# O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) >> 1
            if nums[mid] == nums[l]:
                l += 1
            elif nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
# 192/192 cases passed (48 ms)
# Your runtime beats 97.99 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.1 MB)
# @lc code=end

print(Solution().findMin([10,1,10,10,10]))