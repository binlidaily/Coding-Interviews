#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
# Time: O(n^2)
# Space: O(1)
# class Solution:
#     def minFlipsMonoIncr(self, S: str) -> int:
#         if not S or len(S) == 0:
#             return 0
#         n = len(S)
#         min_flips = float('inf')
#         for i in range(n):
#             cnt, cnt0, cnt1 = 0, 0, 0
#             for j in range(i):
#                 if S[j] == '1':
#                     cnt += 1
#             for l in range(i, n):
#                 if S[l] == '0':
#                     cnt += 1
#             for m in range(n):
#                 if S[m] == '0':
#                     cnt0 += 1
#                 else:
#                     cnt1 += 1
#             min_flips = min(min_flips, cnt, cnt0, cnt1)
#         return min_flips
# TLE


# 1. DP
# Time: O(n)
# Space: O(n)
# class Solution:
#     def minFlipsMonoIncr(self, S: str) -> int:
#         if not S or len(S) == 0:
#             return 0
#         n = len(S)
#         l = [0 for _ in range(n + 1)]
#         r = [0 for _ in range(n + 1)]
#         l[0] = 1 if S[0] == '1' else 0
#         r[n - 1] = 1 if S[n - 1] == '0' else 0
        
#         for i in range(1, n):
#             l[i] = l[i-1] + (1 if S[i] == '1' else 0)
        
#         for i in range(n-2, -1, -1):
#             r[i] = r[i+1] + (1 if S[i] == '0' else 0)
        
#         min_flips = r[0]
#         for i in range(1, n + 1):
#             min_flips = min(min_flips, l[i - 1] + r[i])
#         return min_flips

# 81/81 cases passed (108 ms)
# Your runtime beats 15.62 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (14.3 MB)

# 2. 2D-DP
# Time: O(n)
# Sapce: O(n)
# class Solution:
#     def minFlipsMonoIncr(self, S: str) -> int:
#         if not S or len(S) == 0:
#             return 0
#         n = len(S)
#         dp = [[0 for _ in range(2)] for _ in range(n + 1)]
#         for i in range(1, n+1):
#             if S[i - 1] == '1':
#                 dp[i][0] = dp[i-1][0] + 1
#                 dp[i][1] = min(dp[i-1][0], dp[i-1][1])
#             else:
#                 dp[i][0] = dp[i-1][0]
#                 dp[i][1] = min(dp[i-1][0], dp[i - 1][1]) + 1
#         return min(dp[n][0], dp[n][1])
# 81/81 cases passed (144 ms)
# Your runtime beats 5.8 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (15.4 MB)

# 3. Optimized DP
# Time: O(n)
# Sapce: O(n)
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        if not S or len(S) == 0:
            return 0
        n = len(S)
        dp0, dp1 = 0, 0
        for i in range(1, n+1):
            tmp0 = dp0 + (1 if S[i-1] == '1' else 0)
            dp1 = min(dp0, dp1) + (1 if S[i-1] == '0' else 0)
            dp0 = tmp0
        return min(dp0, dp1)
# 81/81 cases passed (144 ms)
# Your runtime beats 5.8 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (15.4 MB)
# @lc code=end

print(Solution().minFlipsMonoIncr('00011000')) # 2
print(Solution().minFlipsMonoIncr('010110')) # 2
print(Solution().minFlipsMonoIncr('00110')) # 1
print(Solution().minFlipsMonoIncr("11011")) # 1