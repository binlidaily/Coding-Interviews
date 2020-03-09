#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (49.44%)
# Likes:    390
# Dislikes: 27
# Total Accepted:    23.5K
# Total Submissions: 47.5K
# Testcase Example:  '1\n6\n3'
#
# You have d dice, and each die has f faces numbered 1, 2, ..., f.
# 
# Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to
# roll the dice so the sum of the face up numbers equals target.
# 
# 
# Example 1:
# 
# 
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation: 
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
# 
# 
# Example 2:
# 
# 
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation: 
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# 
# 
# Example 3:
# 
# 
# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation: 
# You throw two dice, each with 5 faces.  There is only one way to get a sum of
# 10: 5+5.
# 
# 
# Example 4:
# 
# 
# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation: 
# You throw one die with 2 faces.  There is no way to get a sum of 3.
# 
# 
# Example 5:
# 
# 
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation: 
# The answer must be returned modulo 10^9 + 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= d, f <= 30
# 1 <= target <= 1000
# 
#

# @lc code=start
# 1. DP - Bottom Up
# Time: O(df*target)
# Space: O(d*target)
class Solution1:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 10 ** 9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1

        for i in range(1, d + 1):
            for j in range(1, target + 1):
                lp = min(j, f)
                for k in range(1, lp + 1):
                    dp[i][j] += dp[i - 1][j - k]
        return dp[d][target] % modulo

# 65/65 cases passed (908 ms)
# Your runtime beats 23.63 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.1 MB)

# 2. DP - Top Dwon
# Time: O(df*target)
# Space: O(target)
from functools import lru_cache
class Solution2:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 10**9 + 7
        @lru_cache(maxsize=None)
        def dynamic_programming(i, t):
            if i == 0:
                return 1 if t == 0 else 0
            lp = min(t, f)
            ans = 0
            for j in range(1, lp + 1):
                ans = (ans + dynamic_programming(i-1, t-j))
            return ans
        
        return dynamic_programming(d, target) % modulo

# 65/65 cases passed (348 ms)
# Your runtime beats 70.31 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (19.8 MB)

# 3. DP - Roll Array
# Time: O(df*target)
# Space: O(target)
from functools import lru_cache
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 10**9 + 7
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, d + 1):
            for k in range(target, -1, -1):
                dp[k] = 0
                lp = min(f, k)
                for j in range(1, lp + 1):
                    dp[k] = (dp[k] + dp[k-j])  % modulo
        return dp[target]

# 65/65 cases passed (760 ms)
# Your runtime beats 31.54 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

