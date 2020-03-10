#
# @lc app=leetcode id=391 lang=python3
#
# [391] Perfect Rectangle
#
# https://leetcode.com/problems/perfect-rectangle/description/
#
# algorithms
# Hard (29.58%)
# Likes:    309
# Dislikes: 63
# Total Accepted:    22.5K
# Total Submissions: 76.1K
# Testcase Example:  '[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]'
#
# Given N axis-aligned rectangles where N > 0, determine if they all together
# form an exact cover of a rectangular region.
# 
# Each rectangle is represented as a bottom-left point and a top-right point.
# For example, a unit square is represented as [1,1,2,2]. (coordinate of
# bottom-left point is (1, 1) and top-right point is (2, 2)).
# 
# 
# 
# Example 1:
# 
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4],
# ⁠ [1,3,2,4],
# ⁠ [2,3,3,4]
# ]
# 
# Return true. All 5 rectangles together form an exact cover of a rectangular
# region.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# rectangles = [
# ⁠ [1,1,2,3],
# ⁠ [1,3,2,4],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4]
# ]
# 
# Return false. Because there is a gap between the two rectangular
# regions.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 3:
# 
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [3,2,4,4]
# ]
# 
# Return false. Because there is a gap in the top center.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 4:
# 
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [2,2,4,4]
# ]
# 
# Return false. Because two of the rectangles overlap with each other.
# 
# 
# 
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution1:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        hs = set()
        area = 0
        for rec in rectangles:
            top_left = (rec[0], rec[1])
            top_right = (rec[0], rec[3])
            bottom_left = (rec[2], rec[1])
            bottom_right = (rec[2], rec[3])
            area += (rec[2] - rec[0]) * (rec[3] - rec[1])
            for i in [top_left, top_right, bottom_left, bottom_right]:
                if i not in hs:
                    hs.add(i)
                else:
                    hs.remove(i)
        if len(hs) != 4:
            return False
        hs = sorted(hs)
        first = hs.pop(0)
        last = hs.pop()
        return area == (last[0] - first[0]) * (last[1] - first[1])

# 46/46 cases passed (372 ms)
# Your runtime beats 81.42 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (19.7 MB)

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        #除了四个顶点之外小矩形的顶点成对出现
        lookup = set()
        area = 0
        x_min, y_min, x_max, y_max = float('inf'), float('inf'), -float('inf'), -float('inf')
        for x1, y1, x2, y2 in rectangles:
            x_min = min(x_min, x1)
            y_min = min(y_min, y1)
            x_max = max(x_max, x2)
            y_max = max(y_max, y2)
            area += (y2 - y1) * (x2 - x1)
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in lookup:
                    lookup.remove(point)
                else:
                    lookup.add(point)
        if len(lookup) != 4 or (x_min, y_min) not in lookup or (x_min, y_max) not in lookup \
        or (x_max, y_min) not in lookup or (x_max, y_max) not in lookup:
            return False
        return area == (y_max - y_min) * (x_max - x_min)

# 46/46 cases passed (372 ms)
# Your runtime beats 81.42 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (19.7 MB)
# @lc code=end

