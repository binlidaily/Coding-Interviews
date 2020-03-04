#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
from typing import List
# @lc code=start
# Time: O(logn)
# Space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start, end = -1, -1
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r - l) // 2 
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] != target:
            return [-1, -1]
        else:
            start = l
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2 + 1 # take care of this calculation of mid, need +1 here
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        end = r
        return [start, end]
# 88/88 cases passed (88 ms)
# Your runtime beats 68.21 % of python3 submissions
# Your memory usage beats 8.93 % of python3 submissions (14 MB)

# @lc code=end

print(Solution().searchRange([5,7,7,8,8,10], 8))
print(Solution().searchRange([2,2], 2))