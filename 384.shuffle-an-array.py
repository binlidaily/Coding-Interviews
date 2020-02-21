#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#
from typing import List

# @lc code=start
# Time: O(n)
# Space: O(n)
from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.nums)
        nums = self.nums[:]
        for i in range(n):
            j = randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]
        return nums
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# Time Limit Exceeded
# 2/10 cases passed (N/A)

# 10/10 cases passed (324 ms)
# Your runtime beats 64.42 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (18.1 MB)
# @lc code=end

