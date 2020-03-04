#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         n = len(nums)
#         dp = [1 for _ in range(n)]
#         for i in range(n):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)
# 24/24 cases passed (1224 ms)
# Your runtime beats 21.57 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)

# 2. DP+Binary Search
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         tails = [0] * len(nums)
#         size = 0
#         for x in nums:
#             i, j = 0, size
#             while i != j:
#                 m = (i + j) >> 1
#                 if tails[m] < x:
#                     i = m + 1
#                 else:
#                     j = m
#             tails[i] = x
#             size = max(i + 1, size)
#         return size
# 24/24 cases passed (44 ms)
# Your runtime beats 79.38 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13 MB)

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []
        n = len(nums)
        for i in range(n):
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) >> 1
                if tails[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if right >= len(tails):
                tails.append(nums[i])
            else:
                tails[left] = nums[i]
        return len(tails)
# 24/24 cases passed (44 ms)
# Your runtime beats 79.38 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))