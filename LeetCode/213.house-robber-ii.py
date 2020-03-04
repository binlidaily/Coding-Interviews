#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums or len(nums) <= 0:
#             return 0
#         elif len(nums) == 1:
#             return nums[0]
#         elif len(nums) == 2:
#             return max(nums[0], nums[1])
#         n = len(nums)
#         dp0 = [0 for _ in range(n+1)]
#         dp1 = [0 for _ in range(n+1)]
#         dp0[1] = nums[0]
#         # dp1[1] = nums[1]
#         for i in range(2, n+1):
#             dp0[i] = max(dp0[i-1], dp0[i-2]+nums[i-1])
#             dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i-1])
#         return max(dp0[n-1], dp1[n])

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        n = len(nums)
        dp0 = [0 for _ in range(n)]
        dp1 = [0 for _ in range(n)]
        dp0[0] = nums[0]
        dp0[1] = nums[0]
        dp1[1] = nums[1]
        for i in range(2, n):
            dp0[i] = max(dp0[i-1], dp0[i-2]+nums[i])
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        return max(dp0[-2], dp1[-1])
# 74/74 cases passed (32 ms)
# Your runtime beats 83.6 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,3,2]))
print(Solution().rob([4,1,2,7,5,3,1]))