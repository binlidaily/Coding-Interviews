#
# @lc app=leetcode id=982 lang=python3
#
# [982] Triples with Bitwise AND Equal To Zero
#
from typing import List
# @lc code=start
# Time: O(n^3)
# Space: O(n^2)
# class Solution:
#     def countTriplets(self, A: List[int]) -> int:
#         n = 1 << 16
#         m = 3
#         dp = [[0 for _ in range(n)] for _ in range(m + 1)]
#         dp[0][n-1] = 1
#         for i in range(m):
#             for j in range(n):
#                 for a in A:
#                     dp[i + 1][j & a] += dp[i][j]
#         return dp[m][0]
# Time Limit Exceeded
# 21/25 cases passed (N/A)


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        n = 1 << 16
        m = 3
        dp = [[0 for _ in range(n)] for _ in range(m + 1)]
        for a in A:
            dp[1][a] += 1
        for i in range(1, m):
            for j in range(n):
                if dp[i][j]:
                    for a in A:
                        dp[i + 1][j & a] += dp[i][j]
        return dp[m][0]
# 25/25 cases passed (11348 ms)
# Your runtime beats 7.14 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.9 MB)
# @lc code=end

