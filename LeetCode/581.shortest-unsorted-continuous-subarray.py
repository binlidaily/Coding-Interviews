#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
from typing import List
# @lc code=start
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         copy = [num for num in nums]
#         n = len(nums)
#         self.quick_sort(nums, 0, n-1)
#         min_i, max_i = 0, 0
#         for i in range(n):
#             if nums[i] != copy[i]:
#                 min_i = i
#                 break
        
#         for i in range(n-1, -1, -1):
#             if nums[i] != copy[i]:
#                 max_i = i
#                 break
#         if max_i == min_i:
#             return 0
#         return max_i - min_i + 1
    
#     def quick_sort(self, nums, l=0, r=None):
#         if l > r:
#             return
#         pivot = self.partition(nums, l, r)
#         self.quick_sort(nums, l, pivot-1)
#         self.quick_sort(nums, pivot+1, r)
    
#     def partition(self, nums, l, r):
#         pivot = nums[r]
#         i = l
#         for j in range(l, r+1):
#             if nums[j] < pivot:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#         nums[i], nums[r] = nums[r], nums[i]
#         return i

# 2. O(n)
# Time: O(n)
# Space: O(1)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        max_v, min_v = float('-inf'), float('inf')
        p, q = 0, 0
        for i in range(n):
            if nums[i] >= max_v:
                max_v = nums[i]
            else:
                p = i
        for i in range(n-1, -1, -1):
            if nums[i] <= min_v:
                min_v = nums[i]
            else:
                q = i
        
        if p == q:
            return 0
        return p - q + 1
# 307/307 cases passed (216 ms)
# Your runtime beats 87.91 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.7 MB)
# @lc code=end

print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))