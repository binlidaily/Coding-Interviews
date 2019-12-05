#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(1)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[n]
# 36/36 cases passed (44 ms)
# Your runtime beats 62.15 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

