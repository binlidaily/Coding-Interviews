#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List
import collections
# @lc code=start
# 1. Brute Force - BFS
# Time: O(2^n)
# Space: O(n)
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         res = [0]
#         self.dfs(nums, 0, S, res)
#         return res[0]
    
#     def dfs(self, nums, i, S, res):
#         if i == len(nums):
#             if S == 0:
#                 res[0] += 1
#             return
#         self.dfs(nums, i + 1, S + nums[i], res)
#         self.dfs(nums, i + 1, S - nums[i], res)

# Time Limit Exceeded
# 51/139 cases passed (N/A)

# 2. DP
# Time: O(n^2)
# Space: O(n^2)
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         if not nums:
#             return 0
#         all_sum = sum(nums)

#         if all_sum < S or S < -all_sum:
#             return 0
#         n = len(nums)
#         dp = [[0 for _ in range(2 * all_sum + 1)] for _ in range(n + 1)]
#         dp[0][all_sum] = 1
#         left, right = 0, 2 * all_sum + 1
#         for i in range(1, n+1):
#             for j in range(left, right):
#                 if j + nums[i - 1] < right:
#                     dp[i][j] += dp[i - 1][j + nums[i - 1]]
#                 if j - nums[i - 1] >= left:
#                     dp[i][j] += dp[i - 1][j - nums[i - 1]]
#         return dp[n][all_sum + S]

# 139/139 cases passed (1320 ms)
# Your runtime beats 5.01 % of python3 submissions
# Your memory usage beats 91.67 % of python3 submissions (13.1 MB)

# 2.1 dp
# Time: O(n^2)
# Space: O(n^2)
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         if not nums:
#             return 0
#         all_sum = sum(nums)

#         if all_sum < S or S < -all_sum:
#             return 0
#         n = len(nums)
#         dp = [[0 for _ in range(2 * all_sum + 1)] for _ in range(n + 1)]
#         dp[0][all_sum] = 1
#         right = 2 * all_sum + 1
#         for i in range(n):
#             for j in range(nums[i], right - nums[i]):
#                 if dp[i][j]:
#                     dp[i + 1][j + nums[i]] += dp[i][j]
#                     dp[i + 1][j - nums[i]] += dp[i][j]
#         return dp[n][all_sum + S]

# 139/139 cases passed (364 ms)
# Your runtime beats 47.05 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13 MB)

# Time: O(n^2)
# Space: O(n)
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         if not nums:
#             return 0
#         all_sum = sum(nums)

#         if all_sum < S or S < -all_sum:
#             return 0
#         n = len(nums)
#         # dp[i] represents number of possible ways to reach target i
#         dp = [0 for _ in range(2 * all_sum + 1)]
#         dp[all_sum] = 1
#         right = 2 * all_sum + 1
#         for i in range(n):
#             tmp_dp = [0 for _ in range(2 * all_sum + 1)]
#             for j in range(nums[i], right - nums[i]):
#                 if dp[j] != 0:
#                     tmp_dp[j + nums[i]] += dp[j]
#                     tmp_dp[j - nums[i]] += dp[j]
#             dp = tmp_dp
#         return dp[all_sum + S]

# 139/139 cases passed (308 ms)
# Your runtime beats 57.03 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# Time: O(n^2)
# Space: O(n)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        count = collections.Counter({0:1})
        for num in nums:
            step = collections.Counter()
            for cnt in count:
                step[cnt + num] += count[cnt] 
                step[cnt - num] += count[cnt]
            count = step
        return count[S]
# 139/139 cases passed (320 ms)
# Your runtime beats 55.02 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
# @lc code=end

print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))