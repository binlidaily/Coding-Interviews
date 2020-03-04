#
# @lc app=leetcode id=639 lang=python3
#
# [639] Decode Ways II
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in s:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0
# 195/195 cases passed (368 ms)
# Your runtime beats 83.68 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (13.7 MB)
# @lc code=end

