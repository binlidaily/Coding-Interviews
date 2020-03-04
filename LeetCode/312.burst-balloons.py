#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
from typing import List
# @lc code=start
# 1. DP
# Time: O(n^3)
# Space: O(n^2)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for s in range(2, n):
            for l in range(n - s):
                r = l + s
                for k in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], nums[l] * nums[k] * nums[r] + dp[l][k] + dp[k][r])
        return dp[0][n-1]
# 70/70 cases passed (432 ms)
# Your runtime beats 82.17 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.2 MB)
# @lc code=end

print(Solution().maxCoins([3,1,5,8]))   # 167