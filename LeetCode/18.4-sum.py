#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from typing import List
# @lc code=start
# Time: O(n^3)
# Space: O(n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        self.findNums(nums, target, 4, [], res)
        return res

    def findNums(self, nums, target, n, path, res):
        if len(nums) < n or n < 2:
            return
        
        # solve 2 sum
        if n == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append(path + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - n + 1):   # careful about the range
                if target < nums[i] * n or target > nums[-1] * n:
                    break
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):    # recursively reduce N
                    self.findNums(nums[i+1:], target - nums[i], n - 1, path+[nums[i]], res)
        
        return
# 282/282 cases passed (96 ms)
# Your runtime beats 84.38 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))