#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
# 62/62 cases passed (48 ms)
# Your runtime beats 73.28 % of python3 submissions
# Your memory usage beats 98.51 % of python3 submissions (13.5 MB)

# @lc code=end

print(Solution().searchInsert([1,3,5,6], 5))  # 2