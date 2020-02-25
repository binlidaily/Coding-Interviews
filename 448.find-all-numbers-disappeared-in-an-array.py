#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             idx = abs(nums[i]) - 1
#             nums[idx] = - abs(nums[idx])
#         return [i + 1 for i in range(n) if nums[i] > 0]

# 34/34 cases passed (412 ms)
# Your runtime beats 40.21 % of python3 submissions
# Your memory usage beats 46.43 % of python3 submissions (20.5 MB)

# Time: O(n)
# Space: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        res = []
        for i in range(1, n+1):
            if i not in nums_set:
                res.append(i)
        return res

# 34/34 cases passed (356 ms)
# Your runtime beats 94.57 % of python3 submissions
# Your memory usage beats 7.14 % of python3 submissions (22.8 MB)
# @lc code=end

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))