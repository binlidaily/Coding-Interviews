#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_gap = float('inf')
        res = None
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                thd_sum = nums[i] + nums[l] + nums[r]
                if thd_sum == target:
                    return target
                elif thd_sum < target:
                    l += 1
                else:
                    r -= 1
                gap = abs(thd_sum - target)
                if gap < min_gap:
                    res = thd_sum
                    min_gap = gap
        return res

# 125/125 cases passed (96 ms)
# Your runtime beats 94.34 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().threeSumClosest([-1, 2, 1, -4], 1))