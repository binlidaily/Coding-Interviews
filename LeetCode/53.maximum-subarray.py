#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.70%)
# Likes:    6842
# Dislikes: 310
# Total Accepted:    875.1K
# Total Submissions: 1.9M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
from typing import List
# Time: O(n)
# Space: O(n)
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
            max_sum = max(max_sum, dp[i])
        return max_sum

# 202/202 cases passed (72 ms)
# Your runtime beats 28.46 % of python3 submissions
# Your memory usage beats 5.69 % of python3 submissions (14.7 MB)

# 2. DP - rolling array
# Time: O(n)
# Space: O(1)
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max_end_i = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            dp_max_end_i = nums[i] + (dp_max_end_i if dp_max_end_i > 0 else 0)
            max_sum = max(max_sum, dp_max_end_i)
        return max_sum

# 202/202 cases passed (64 ms)
# Your runtime beats 82.31 % of python3 submissions
# Your memory usage beats 5.69 % of python3 submissions (14.7 MB)


# Time: O(n)
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            if cur_sum <= 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)

        return max_sum

# 202/202 cases passed (60 ms)
# Your runtime beats 94.35 % of python3 submissions
# Your memory usage beats 5.69 % of python3 submissions (14.6 MB)
# @lc code=end

