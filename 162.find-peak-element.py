#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
from typing import List
# @lc code=start
# Time: O(logn)
# Space: O(1)
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         if not nums:
#             return -1

#         n = len(nums)
#         if n == 1:
#             return 0
#         l, r = 0, n - 1
#         while l < r-1:
#             mid = l + (r - l) // 2
#             if nums[mid-1] < nums[mid] > nums[mid+1]:
#                 return mid
#             if nums[mid+1] > nums[mid]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return l if nums[l] > nums[r] else r
# 59/59 cases passed (40 ms)
# Your runtime beats 91.44 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)


# 2. pattern
# Time: O(logn)
# Space: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid  # verify it with examples
        return l # the left number!
# 59/59 cases passed (44 ms)
# Your runtime beats 72.82 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=end

print(Solution().findPeakElement([1,2,3,1]))