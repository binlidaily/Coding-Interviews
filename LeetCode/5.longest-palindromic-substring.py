#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
# Time: O(n^2)
# Sapce: O(n^2)
class Solution(object):
    def longestPalindrome(self, s):
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        l, r = 0, 0
        
        for i in range(len(s)):
            start = i
            end = i
            while start >= 0:
                # only one center number
                if start == end:
                    dp[start][end] = True
                # two center numbers
                elif start + 1 == end:
                    dp[start][end] = s[start] == s[end]
                # state tranformation equation
                else:
                    dp[start][end] = dp[start + 1][end - 1] and (s[start] == s[end])
                
                if dp[start][end] and (end - start + 1) > (r - l + 1):
                    l = start
                    r = end
                start = start - 1
        return s[l:r + 1]


# @lc code=end