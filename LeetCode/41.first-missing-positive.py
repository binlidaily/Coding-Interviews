#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         n = len(nums)
#         for i in range(n):
#             while nums[i] > 0 and nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
#                 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

#         for i in range(n):
#             if nums[i] != i + 1:
#                 return i + 1
#         return n + 1

# 165/165 cases passed (36 ms)
# Your runtime beats 48.81 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 1
        
#         large = max(nums)
        
#         if large < 0:
#             return 1
        
#         for i in range(1, large + 1):
#             if i not in nums:
#                 return i
#         return large + 1
# 165/165 cases passed (36 ms)
# Your runtime beats 48.81 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# Time: O(n)
# Space: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] != i + 1 and nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]-1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i+1
        return n + 1

# 165/165 cases passed (32 ms)
# Your runtime beats 79.23 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().firstMissingPositive([3,4,-1,1]))