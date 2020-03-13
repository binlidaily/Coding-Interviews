#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#
# https://leetcode.com/problems/random-pick-index/description/
#
# algorithms
# Medium (53.19%)
# Likes:    363
# Dislikes: 583
# Total Accepted:    72.3K
# Total Submissions: 135.6K
# Testcase Example:  '["Solution","pick"]\n[[[1,2,3,3,3]],[3]]'
#
# Given an array of integers with possible duplicates, randomly output the
# index of a given target number. You can assume that the given target number
# must exist in the array.
# 
# Note:
# The array size can be very large. Solution that uses too much extra space
# will not pass the judge.
# 
# Example:
# 
# 
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# 
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should
# have equal probability of returning.
# solution.pick(3);
# 
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
# 
# 
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution1:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        idx = []
        for i, num in enumerate(self.nums):
            if num == target:
                idx.append(i)
        import random
        return random.choice(idx)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# 13/13 cases passed (300 ms)
# Your runtime beats 94.99 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (16.7 MB)


# Time: O(n)
# Space: O(n)
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        import random
        res = -1
        count = 0
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1 
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res

# 13/13 cases passed (312 ms)
# Your runtime beats 78.28 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (16.7 MB)
# @lc code=end

