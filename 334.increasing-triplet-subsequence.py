#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
from typing import List
# @lc code=start
# 1. DP - ETL
# Time: O(n^2)
# Space: O(n)
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         if not nums or len(nums) < 3:
#             return False
#         n = len(nums)
#         dp = [1 for i in range(n)]
#         for i in range(n):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[j] + 1, dp[i])
#                     if dp[i] >= 3:
#                         return True
#         return False
# Time Limit Exceeded
# 61/62 cases passed (N/A)

# Time: O(n)
# Space: O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        n = len(nums)
        first = second = float('inf')
        for i in range(n):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        return False
# 62/62 cases passed (52 ms)
# Your runtime beats 82.14 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.2 MB)
# @lc code=end

print(Solution().increasingTriplet([1,2,3,4,5]))    # True
print(Solution().increasingTriplet([5,4,3,2,1]))    # False