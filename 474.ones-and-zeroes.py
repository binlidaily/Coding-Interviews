#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
from typing import List
# @lc code=start
# Time: O(lmn)
# Space: O(lmn)
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         l = len(strs)
#         # dp[l+1][m+1][n+1]
#         dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(l + 1)]
#         for i in range(1, l + 1):
#             s = strs[i - 1]
#             size = len(s)
#             zeros = s.count('0')
#             ones = size - zeros
#             for j in range(0, m + 1):
#                 for k in range(0, n + 1):
#                     if zeros <= j and ones <= k:
#                         dp[i][j][k] = max(dp[i - 1][j][k], 1 + dp[i - 1][j - zeros][k - ones])
#                     else:
#                         dp[i][j][k] = dp[i - 1][j][k]
#         return dp[l][m][n]
# Runtime: 5136 ms, faster than 13.59%
# Memory Usage: 61.1 MB, less than 100.00%

# Time: O(lmn)
# Space: O(mn)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[m+1][n+1]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            size = len(s)
            zeros = s.count('0')
            ones = size - zeros
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if zeros <= j and ones <= k:
                        dp[j][k] = max(dp[j][k], 1 + dp[j - zeros][k - ones])
        return dp[m][n]
# Runtime: 3908 ms, faster than 26.48%
# Memory Usage: 12.9 MB, less than 100.00%
# @lc code=end

print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], m = 5, n = 3))
print(Solution().findMaxForm(["10","0","1"], m = 1, n = 1))

