#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        dp[0] = nums[0]
        for i in range(1, n+1):
            if i - 2 > 0:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            else:
                dp[i] = max(dp[i-1], nums[i-1])
        print(dp)
        return dp[n]
# 69/69 cases passed (28 ms)
# Your runtime beats 93.36 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
# @lc code=end


print(Solution().rob([1,2,3,1]))
print(Solution().rob([1,1]))
print(Solution().rob([1,2]))