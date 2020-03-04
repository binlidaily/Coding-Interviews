#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List
# @lc code=start
# Time: O(mn)
# Space: O(mn)
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         if not nums:
#             return False
#         sumA = sum(nums)
#         # if the sum is odd, return False
#         if sumA & 1 == 1:
#             return False
#         sumA = sumA >> 1
#         n = len(nums)
#         dp = [[False for _ in range(sumA + 1)] for _ in range(n + 1)]
#         dp[0][0] = True
#         for i in range(1, n + 1):
#             dp[i][0] = True
#         for j in range(1, sumA + 1):
#             dp[0][j] = False
#         for i in range(1, n + 1):
#             for j in range(1, sumA + 1):
#                 if nums[i - 1] <= j:
#                     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
#                 else:
#                     dp[i][j] = dp[i - 1][j]
#         return dp[n][sumA]
# Runtime: 2180 ms, faster than 10.05%
# Memory Usage: 16.8 MB, less than 9.09%

# Time: O(mn)
# Space: O(m)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        sumA = sum(nums)
        # if the sum is odd, return False
        if sumA & 1 == 1:
            return False
        sumA = sumA >> 1
        dp = [False for _ in range(sumA + 1)]
        dp[0] = True
        
        for num in nums:
            for j in range(sumA, -1, -1):
                if num <= j:
                    dp[j] = dp[j] or dp[j - num]
        return dp[sumA]
# Runtime: 884 ms, faster than 42.07%
# Memory Usage: 12.7 MB, less than 100.00% 
# @lc code=end

print(Solution().canPartition([1, 5, 11, 5]))  # True
print(Solution().canPartition([1, 2, 3, 5]))  # False
print(Solution().canPartition([23,13,11,7,6,5,5]))  # True
print(Solution().canPartition([1,2,5]))  # False

