#
# @lc app=leetcode id=730 lang=python3
#
# [730] Count Different Palindromic Subsequences
#

# @lc code=start
# Time complexity: O(n^2)
# Space complexity: O(n^2)
# class Solution:
#     def countPalindromicSubsequences(self, S: str) -> int:
#         n = len(S)
#         self.m_ = [[None for _ in range(n)] for _ in range(n)]
#         return self.count(S, 0, n - 1)

#     def count(self, S, i, j):
#             if i > j: return 0
#             if i == j: return 1
#             if self.m_[i][j]: return self.m_[i][j]
 
#             if S[i] == S[j]:
#                 ans = self.count(S, i + 1, j - 1) * 2
#                 l = i + 1
#                 r = j - 1
#                 while l <= r and S[l] != S[i]: l += 1
#                 while l <= r and S[r] != S[i]: r -= 1
#                 if l > r: ans += 2
#                 elif l == r: ans += 1
#                 else: ans -= self.count(S, l + 1, r - 1)                
#             else:
#                 ans = self.count(S, i + 1, j) + self.count(S, i, j - 1) - self.count(S, i + 1, j - 1)
 
#             self.m_[i][j] = ans % 1000000007
#             return self.m_[i][j]
# 366/366 cases passed (2208 ms)
# Your runtime beats 39.86 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (31.3 MB)

# 2. DP
class Solution:
    def countPalindromicSubsequences(self, S):        
        n = len(S)
        if n == 0: return 0        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): dp[i][i] = 1
            
        for size in range(2, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1                
                if S[i] == S[j]:
                    dp[i][j] = dp[i + 1][j - 1] * 2
                    l = i + 1
                    r = j - 1
                    while l <= r and S[l] != S[i]: l += 1
                    while l <= r and S[r] != S[i]: r -= 1
                    if l > r: dp[i][j] += 2
                    elif l == r: dp[i][j] += 1
                    else: dp[i][j] -= dp[l + 1][r - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] 
                dp[i][j] %= 1000000007
            
        return dp[0][n - 1]
# 366/366 cases passed (2124 ms)
# Your runtime beats 40.56 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (36.7 MB)
# @lc code=end

