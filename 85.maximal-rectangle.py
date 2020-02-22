#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
from typing import List
# @lc code=start
# 1. monotonic stack
# Time: O(mn)
# Space: O(n)
# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         if not matrix or len(matrix) == 0:
#             return 0
#         r, c = len(matrix), len(matrix[0])
#         heights = [0 for _ in range(c)]
#         max_rect = 0
#         for row in matrix:
#             for i in range(c):
#                 if row[i] == '0':
#                     heights[i] = 0
#                 else:
#                     heights[i] += 1
#             max_rect = max(max_rect, self.largestRectangleArea(heights))
#         return max_rect
    
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         if not heights:
#             return 0
#         n = len(heights)
#         stack = []
#         max_area = 0
#         i = 0
#         while i <= n: 
#             h = 0 if i == n else heights[i]
#             if (not stack) or h >= heights[stack[-1]]:
#                 stack.append(i)
#                 i += 1
#             else:
#                 height = heights[stack.pop()]
#                 r_i = i - 1
#                 l_i = (stack[-1] + 1) if stack else 0  # add 1 becuase pop first
#                 width = r_i - l_i + 1 
#                 max_area = max(max_area, height*width)
#         return max_area
# Runtime: 204 ms, faster than 90.33%
# Memory Usage: 13.7 MB, less than 100.00%

# Time: O(mn*n)
# Space: O(nm)
# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0
#         r, c = len(matrix), len(matrix[0])
#         # dp[i][j] := max length of all 1 sequence ends with col j, at the i-th row.
#         dp = [[0 for _ in range(c)] for _ in range(r)]
#         # Transition
#         for i in range(r):
#             for j in range(c):
#                 if matrix[i][j] == '1':
#                     if j == 0:
#                         dp[i][j] = 1
#                     else:
#                         dp[i][j] = dp[i][j-1] + 1
#                 # elif matrix[i][j] == '0':
#                 #     dp[i][j] = 0
#         res = 0
#         for i in range(r):
#             for j in range(c):
#                 size = float('inf')
#                 for k in range(i, r):
#                     size = min(size, dp[k][j])
#                     if size == 0:
#                         break
#                     res = max(size * (k - i + 1), res)
#         return res

# 66/66 cases passed (476 ms)
# Your runtime beats 18.15 % of python3 submissions
# Your memory usage beats 93.75 % of python3 submissions (13.8 MB)

# 1 0 1 0 0      1 0 1 0 0
# 1 0 1 1 1  =>  2 0 2 1 1
# 1 1 1 1 1  =>  3 1 3 2 2
# 1 0 0 1 0      4 0 0 3 0
# Time: O(mn)
# Space: O(n)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        max_area = 0
        for i in range(r):
            for j in range(c):
                if i == 0:
                    dp[i][j] = 1 if matrix[i][j] == '1' else 0
                else:
                    if matrix[i][j] == '1':
                        dp[i][j] = dp[i-1][j] + 1
                    else:
                        dp[i][j] = 0
                min_col = dp[i][j]
                for k in range(j, -1, -1):
                    if min_col == 0:
                        break
                    if dp[i][k] < min_col:
                        min_col = dp[i][k]
                    max_area = max(max_area, min_col * (j - k + 1))
        return max_area



# @lc code=end

print(Solution().maximalRectangle([
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
]))