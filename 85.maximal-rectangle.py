#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
from typing import List
# @lc code=start
# Time: O(mn)
# Space: O(n)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0
        r, c = len(matrix), len(matrix[0])
        heights = [0 for _ in range(c)]
        max_rect = 0
        for row in matrix:
            for i in range(c):
                if row[i] == '0':
                    heights[i] = 0
                else:
                    heights[i] += 1
            max_rect = max(max_rect, self.largestRectangleArea(heights))
        return max_rect
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        stack = []
        max_area = 0
        i = 0
        while i <= n: 
            h = 0 if i == n else heights[i]
            if (not stack) or h >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                height = heights[stack.pop()]
                r_i = i - 1
                l_i = (stack[-1] + 1) if stack else 0  # add 1 becuase pop first
                width = r_i - l_i + 1 
                max_area = max(max_area, height*width)
        return max_area
# Runtime: 204 ms, faster than 90.33%
# Memory Usage: 13.7 MB, less than 100.00%
# @lc code=end

