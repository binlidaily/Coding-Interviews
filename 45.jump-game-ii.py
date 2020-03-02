#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from typing import List
# @lc code=start
# Time: O(nm)
# Space: O(n)
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [float('inf')] * n
#         dp[0] = 0
#         for i, num in enumerate(nums):
#             for j in range(1, num+1):
#                 if i + j >= n:
#                     break
#                 dp[i + j] = min(dp[i] + 1, dp[i + j])
#         return dp[n-1]

# Time Limit Exceeded
# 91/92 cases passed (N/A)


# Time: O(nm)
# Space: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        # these two variable store the index which it can reach
        pre_jump_max, cur_jump_max = 0, 0
        for i in range(n):
            cur_jump_max = max(cur_jump_max, i + nums[i])
            if pre_jump_max == n - 1:
                break
            if i == pre_jump_max:
                jumps += 1
                pre_jump_max = cur_jump_max
        return jumps

# 92/92 cases passed (96 ms)
# Your runtime beats 78.9 % of python3 submissions
# Your memory usage beats 8.33 % of python3 submissions (14.9 MB)
# @lc code=end

print(Solution().jump([2,3,1,1,4]))