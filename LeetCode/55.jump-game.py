#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        for i, num in enumerate(nums):
            if max_i < i:
                return False
            max_i = max(max_i, i + num)
        return True

# 75/75 cases passed (84 ms)
# Your runtime beats 93.56 % of python3 submissions
# Your memory usage beats 7.14 % of python3 submissions (14.8 MB)
# @lc code=end

print(Solution().canJump([2,3,1,1,4]))  # True
print(Solution().canJump([3,2,1,0,4]))  # True