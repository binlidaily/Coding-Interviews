#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
# Time: O(mn)
# Space: O(mn)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        dp[0][0] = 0
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n2 + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],  # replace
                                      dp[i-1][j],     # delete
                                      dp[i][j-1])     # insert
        return dp[n1][n2]
# Runtime: 188 ms, faster than 60.15% 
# Memory Usage: 16.4 MB, less than 80.77%
# @lc code=end

print(Solution().minDistance(word1 = "horse", word2 = "ros"))
print(Solution().minDistance(word1 = "intention", word2 = "execution"))
