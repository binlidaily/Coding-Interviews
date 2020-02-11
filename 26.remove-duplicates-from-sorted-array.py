#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 0
#         while i < len(nums):
#             if i > 0 and nums[i-1] == nums[i]:
#                 nums = nums[:i] + nums[i+1:]
#             else:
#                 i += 1
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tail = 0
        n = len(nums)
        for i in range(1, n):
            # Override
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1

# 161/161 cases passed (84 ms)
# Your runtime beats 77.76 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.3 MB)
# @lc code=end

print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))