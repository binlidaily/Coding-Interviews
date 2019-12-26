#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if not nums:
#             return
#         n = len(nums)
#         if k >= n:
#             k %= n
#         self.reverse_list(nums, 0, n-k-1)
#         # print(nums)
#         self.reverse_list(nums, n-k, n-1)
#         # print(nums)
#         self.reverse_list(nums, 0, n-1)
#         # print(nums)
    
#     def reverse_list(self, nums, l, r):
#         if l < 0 or r >= len(nums):
#             return False
#         while l < r:
#             nums[l], nums[r] = nums[r], nums[l]
#             l += 1
#             r -= 1
#         return True
# 34/34 cases passed (72 ms)
# Your runtime beats 58.01 % of python3 submissions
# Your memory usage beats 5.09 % of python3 submissions (14 MB)

# 2. faster
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        if k == 0:
            return
        for i in range(self.gcd(length, k)):
            prev = nums[i]
            j = (i + k) % length
            while j != i:
                next_n = nums[j]
                nums[j] = prev
                prev = next_n
                j = (j+k) % length
            nums[j] = prev
    
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
# 34/34 cases passed (60 ms)
# Your runtime beats 90.55 % of python3 submissions
# Your memory usage beats 5.09 % of python3 submissions (14.2 MB)
# @lc code=end

print(Solution().rotate([1,2,3,4,5,6,7], 3))