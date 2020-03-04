#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0 for _ in range(n)]
        is_pal = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            min_cuts = i
            j = 0
            while j <= i:
                if s[j] == s[i] and (i - j < 2 or is_pal[j + 1][i - 1]):
                    is_pal[j][i] = True
                    min_cuts = 0 if j == 0 else min(min_cuts, dp[j - 1] + 1)
                j += 1
            dp[i] = min_cuts
        return dp[-1]
# 29/29 cases passed (540 ms)
# Your runtime beats 41.7 % of python3 submissions
# Your memory usage beats 80 % of python3 submissions (31.1 MB)

# @lc code=end

print(Solution().minCut('aab'))