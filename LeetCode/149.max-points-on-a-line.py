#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
import collections
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        for i in range(n):
            lines = collections.defaultdict(int)
            duplicates = 1
            for j in range(i+1, n):
                if points[i][0] == points[j][0] and \
                    points[i][1] == points[j][1]:
                    duplicates += 1
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                delta = self.gcd(dx, dy)
                lines[(dx / delta, dy / delta)] += 1
            res = max(res, (max(lines.values()) if lines else 0) + duplicates)
        return res

    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)
# 37/37 cases passed (68 ms)
# Your runtime beats 70.54 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().maxPoints([[1,1],[2,2],[3,3]]))