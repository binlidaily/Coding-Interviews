#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        res = [1 for _ in range(n)]

        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        right_prod = 1
        for i in range(n-2, -1, -1):
            right_prod *= nums[i+1]
            res[i] = res[i] * right_prod
        return res

# 17/17 cases passed (120 ms)
# Your runtime beats 87.45 % of python3 submissions
# Your memory usage beats 96 % of python3 submissions (19.5 MB)
# @lc code=end

print(Solution().productExceptSelf([1,2,3,4]))