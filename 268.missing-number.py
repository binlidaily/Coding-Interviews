#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         sum_nums = sum(nums)
#         sum_full = 0
#         for i in range(len(nums)+1):
#             sum_full += i
#         return sum_full - sum_nums

# 122/122 cases passed (140 ms)
# Your runtime beats 70.74 % of python3 submissions
# Your memory usage beats 83.87 % of python3 submissions (14 MB)

# Time: O(n)
# Space: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(n):
            xor = xor ^ i ^ nums[i]
        return xor ^ n

# 122/122 cases passed (136 ms)
# Your runtime beats 85.31 % of python3 submissions
# Your memory usage beats 90.32 % of python3 submissions (14 MB)
# @lc code=end

print(Solution().missingNumber([3,0,1]))    # 2
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))    # 8