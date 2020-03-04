#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
from typing import List
import collections
# @lc code=start
# 1. Brute Force
# Time: O(n^3)
# Space: O(n)
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         res = 0
#         for i in range(n):
#             for j in range(i, n):
#                 if sum(nums[i:j+1]) == k:
#                     res += 1
#         return res

# Time Limit Exceeded
# 58/80 cases passed (N/A)

# 2. Prefix Sum
# Time: O(n^2)
# Space: O(n)
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         res = 0
#         prefix_sum = [0] * n
#         for i in range(n):
#             prefix_sum[i] = prefix_sum[i-1] + nums[i]

#         for i in range(n):
#             for j in range(i, n):
#                 if prefix_sum[j] - prefix_sum[i] + nums[i] == k:
#                     res += 1
#         return res
# Time Limit Exceeded
# 69/80 cases passed (N/A)

# 2. Hash table
# Time: O(n)
# Space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Keep tracking the prefix sums and their counts
        counts = collections.defaultdict()
        counts[0] = 1
        cur_sum, res = 0, 0
        for num in nums:
            cur_sum += num
            res += counts.get(cur_sum - k, 0)
            counts[cur_sum] = counts.get(cur_sum, 0) + 1
        return res
# 80/80 cases passed (108 ms)
# Your runtime beats 92.07 % of python3 submissions
# Your memory usage beats 96 % of python3 submissions (15.2 MB)
# @lc code=end

print(Solution().subarraySum(nums = [1,1,1], k = 2))