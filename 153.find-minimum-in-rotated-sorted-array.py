#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            mid = (l + r) >> 1
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
# 146/146 cases passed (40 ms)
# Your runtime beats 91.62 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().findMin([3,4,5,1,2]))