#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# @lc code=start
from typing import List
import collections
# Time: O(n^2)
# Space: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) <= 2:
            return []
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            print(i)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                _sum = nums[l] + nums[i] + nums[r]
                if _sum == 0:
                    res.append([nums[l], nums[i], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif _sum < 0:
                    l += 1
                else:
                    r -= 1
        return res
# 313/313 cases passed (984 ms)
# Your runtime beats 53.09 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (16.2 MB)
            
# print(Solution().threeSum([-2,-3,0,0,-2]))

# @lc code=end

