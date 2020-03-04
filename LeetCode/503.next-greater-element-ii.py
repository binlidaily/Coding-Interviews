#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
from typing import List
# @lc code=start
# 1. Brute Force
# Time: O(n^2)
# Space: O(n)
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         if not nums:
#             return []
#         n = len(nums)
#         res = [-1 for _ in range(n)]
#         for i in range(n):
#             j = i + 1
#             while j % n != i:
#                 if nums[i] < nums[j % n]:
#                     res[i] = nums[j % n]
#                     break
#                 j += 1
#         return res
# Time Limit Exceeded
# 223/224 cases passed (N/A)


# 2. Stack
# Time: O(n^2)
# Space: O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        stack = []
        res = [-1 for _ in range(n)]
        for i in range(2*n):
            j = i % n
            while stack and nums[stack[-1]] < nums[j]:
                res[stack.pop()] = nums[j]
            stack.append(j)
        return res
# 224/224 cases passed (232 ms)
# Your runtime beats 86.03 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.2 MB)

# @lc code=end

print(Solution().nextGreaterElements([5,4,3,2,1]))
print(Solution().nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))