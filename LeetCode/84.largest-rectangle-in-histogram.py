#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
from typing import List
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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


# @lc code=end

