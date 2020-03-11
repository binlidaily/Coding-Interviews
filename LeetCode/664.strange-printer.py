#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#
# https://leetcode.com/problems/strange-printer/description/
#
# algorithms
# Hard (39.03%)
# Likes:    345
# Dislikes: 43
# Total Accepted:    12.7K
# Total Submissions: 32.2K
# Testcase Example:  '"aaabbb"'
#
# 
# There is a strange printer with the following two special requirements:
# 
# 
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending
# at any places, and will cover the original existing characters.
# 
# 
# 
# 
# 
# Given a string consists of lower English letters only, your job is to count
# the minimum number of turns the printer needed in order to print it.
# 
# 
# Example 1:
# 
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# 
# 
# 
# Example 2:
# 
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of
# the string, which will cover the existing character 'a'.
# 
# 
# 
# Hint: Length of the given string will not exceed 100.
#

# @lc code=start
# Time: O(n^3)
# Space: O(n^3)
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = 1 if i == j else dp[i+1][j] + 1
                for k in range(i+1, j+1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j])
        return 0 if n == 0 else dp[0][n-1]

# 201/201 cases passed (688 ms)
# Your runtime beats 60.24 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

