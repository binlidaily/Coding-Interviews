#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i, j = 0, 0
#         n = len(nums)
#         while i < n and j < n:
#             while i < n and nums[i] != 0:
#                 i += 1
#             j = i
#             while j < n and nums[j] == 0:
#                 j += 1
#             if i < n and j < n and nums[i] == 0 and nums[j] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#         return nums
# 21/21 cases passed (412 ms)
# Your runtime beats 6.62 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.8 MB)

# Time: O(n)
# Space: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i_zeros = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[i_zeros] = nums[i_zeros], nums[i]
                i_zeros += 1

# 21/21 cases passed (48 ms)
# Your runtime beats 75.7 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.8 MB)


# @lc code=end

print(Solution().moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
print(Solution().moveZeroes([1,0]))  # [1,0]