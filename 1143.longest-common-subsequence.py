#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
# Time: O(mn)
# Space: O(mn)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        n1, n2 = len(text1), len(text2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[n1][n2]
        
# 37/37 cases passed (452 ms)
# Your runtime beats 58.33 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (21.5 MB)
        
# @lc code=end

print(Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace" )) # 3
print(Solution().longestCommonSubsequence(text1 = "abc", text2 = "abc")) # 3
print(Solution().longestCommonSubsequence(text1 = "abc", text2 = "def" )) # 0