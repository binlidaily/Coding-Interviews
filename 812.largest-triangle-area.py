#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#
from typing import List
# @lc code=start
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        if not points or len(points) <= 2:
            return 0
        res = [-1]
        self.dfs(points, 0, [], res)
        return res[0]
    
    def dfs(self, points, start, path, res):
        if path and len(path) >= 3:
            s = 0.5 * abs(path[0][0] * path[1][1] + path[1][0] * path[2][1] + path[2][0] * path[0][1] - path[0][0] * path[2][1] -  path[2][0] * path[1][1] - path[1][0] * path[0][1])
            res[0] = max(s, res[0])
            return
        n = len(points)
        for i in range(start, n):
            self.dfs(points, i+1, path+[points[i]], res)
# @lc code=end

print(Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
print(Solution().largestTriangleArea([[1,0],[0,0],[0,1]]))