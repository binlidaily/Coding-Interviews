#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or s == '':
            return 0
        n = len(s)
        # dp[i] stands for the lenght of longest substring ends with s[i]
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i - 2 >= 0:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                else: # if s[i-1] == ')', combine the previous length.
                    if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                        if i-dp[i-1]-2 >= 0:
                            dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                        else:
                            dp[i] = dp[i-1] + 2
            else:
                continue
        return max(dp)
# Runtime: 56 ms, faster than 37.73%
# Memory Usage: 12.9 MB, less than 100.00%
# @lc code=end

print(Solution().longestValidParentheses('(()'))
print(Solution().longestValidParentheses(')()())'))