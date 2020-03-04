#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        k = n - 2
        while k >= 0 and nums[k] >= nums[k+1]: # to find the largest k with nums[k] < nums[k+1]
            k -= 1
        if k < 0:
            # nums = nums[::-1]     # This cannot copy, just get object
            nums[:] = nums[::-1]
        else:
            l = n - 1
            while l >= 0 and nums[k] >= nums[l]: # to find the smallest l with nums[k] < nums[l]
                l -= 1
            nums[k], nums[l] = nums[l], nums[k] # smallest l on the right which nums[l] > nums[k]
            # orignal decrecing order should be increasing
            nums[k+1:] = nums[k+1:][::-1]   # to 
        return nums

# 265/265 cases passed (40 ms)
# Your runtime beats 69.22 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# @lc code=end

print(Solution().nextPermutation([1,2,3]))  # 1,3,2
print(Solution().nextPermutation([3,2,1]))  # 1,2,3
print(Solution().nextPermutation([1,1,5]))  # 1,5,1
print(Solution().nextPermutation([1,3,2]))  # 2,3,1 -> 2,1,3
print(Solution().nextPermutation([3,2,1]))  # 3,2,1 -> 1,2,3