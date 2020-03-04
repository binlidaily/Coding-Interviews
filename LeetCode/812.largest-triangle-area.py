#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#
from typing import List
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
# class Solution:
#     def largestTriangleArea(self, points: List[List[int]]) -> float:
#         if not points or len(points) <= 2:
#             return 0
#         res = [-1]
#         self.dfs(points, 0, [], res)
#         return res[0]
    
#     def dfs(self, points, start, path, res):
#         if path and len(path) >= 3:
#             s = 0.5 * abs(path[0][0] * path[1][1] + path[1][0] * path[2][1] + path[2][0] * path[0][1] - path[0][0] * path[2][1] -  path[2][0] * path[1][1] - path[1][0] * path[0][1])
#             res[0] = max(s, res[0])
#             return
#         n = len(points)
#         for i in range(start, n):
#             self.dfs(points, i+1, path+[points[i]], res)
# 57/57 cases passed (268 ms)
# Your runtime beats 29.53 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)


# 2. Math

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
            for i, j, k in itertools.combinations(points, 3))
# 57/57 cases passed (136 ms)
# Your runtime beats 77.17 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
print(Solution().largestTriangleArea([[1,0],[0,0],[0,1]]))