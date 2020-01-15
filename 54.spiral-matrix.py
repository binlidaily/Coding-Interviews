#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import List
# @lc code=start
# Time: O(mn)
# Space: O(n)
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
#         while matrix:
#             res += matrix.pop(0)  # left to right
#             if matrix and matrix[0]:  # top to down
#                 for row in matrix:
#                     res.append(row.pop())
#             if matrix:  # right to left
#                 res += matrix.pop()[::-1]
#             if matrix and matrix[0]:  # bottom to up
#                 for row in matrix[::-1]:
#                     res.append(row.pop(0))
#         return res
# 22/22 cases passed (28 ms)
# Your runtime beats 61 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# 2. keep matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        
        while True:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if left > right or top > bottom:
                break
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right or top > bottom:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if left > right or top > bottom:
                break
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right or top > bottom:
                break
        return res
# 22/22 cases passed (28 ms)
# Your runtime beats 61 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

