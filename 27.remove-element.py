#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         if not nums:
#             return 0
#         i = 0
#         while i < len(nums):
#             if nums[i] == val:
#                 del nums[i]
#             else:
#                 i += 1
#         return len(nums)

# 113/113 cases passed (32 ms)
# Your runtime beats 58.17 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# 2. Two pointers
# Time: O(n)
# Space: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        fast, slow = 0, 0
        n = len(nums)
        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

# 113/113 cases passed (28 ms)
# Your runtime beats 84.6 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().removeElement(nums = [3,2,2,3], val = 3))
print(Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))