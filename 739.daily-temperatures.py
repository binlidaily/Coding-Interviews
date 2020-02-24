#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(1)
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         n = len(T)
#         res = []
#         for i in range(n-1):
#             gap = 0
#             for j in range(i+1, n):
#                 if T[i] < T[j]:
#                     gap = j - i
#                     break
#             res.append(gap)
#         res.append(0)
#         return res

# Time Limit Exceeded
# 28/37 cases passed (N/A)

# Time: O(n)
# Space: O(n)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        stack = []
        res = [0] * n
        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

# 37/37 cases passed (492 ms)
# Your runtime beats 76.4 % of python3 submissions
# Your memory usage beats 55.26 % of python3 submissions (16.7 MB)
# @lc code=end

print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))   # [1, 1, 4, 2, 1, 1, 0, 0]