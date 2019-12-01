#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#
from typing import List
# @lc code=start
## 1. DFS, Backtracking
# Time: O(4^{mn})
# Space: O(m*n)
# class Solution:
#     def uniquePathsIII(self, grid: List[List[int]]) -> int:
#         res = [0]
#         self.m, self.n, empty = len(grid), len(grid[0]),1
#         for i in range(self.m):
#             for j in range(self.n):
#                 if grid[i][j] == 1: x,y = (i, j)
#                 elif grid[i][j] == 2: self.end = (i, j)
#                 elif grid[i][j] == 0: empty += 1
#         self.dfs(grid, x, y, empty, res)
#         return res[0]
#     def dfs(self, grid, x, y, empty, res):
#             if not (0 <= x < self.m and 0 <= y < self.n and grid[x][y] >= 0): return
#             if (x, y) == self.end:
#                 res[0] += empty == 0
#                 return
#             grid[x][y] = -2
#             self.dfs(grid, x + 1, y, empty - 1, res)
#             self.dfs(grid, x - 1, y, empty - 1, res)
#             self.dfs(grid, x, y + 1, empty - 1, res)
#             self.dfs(grid, x, y - 1, empty - 1, res)
#             grid[x][y] = 0
# 39/39 cases passed (56 ms)
# Your runtime beats 88.68 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)


## 2. DP
from functools import lru_cache
# Time: O(m*n*2^{m*n})
# Space: O(m*n)
class Solution:
    def uniquePathsIII(self, grid):
        R, C = len(grid), len(grid[0])

        def code(r, c):
            return 1 << (r * C + c)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        target = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val % 2 == 0:
                    target |= code(r, c)

                if val == 1:
                    sr, sc = r, c
                if val == 2:
                    tr, tc = r, c

        @lru_cache(None)
        def dp(r, c, todo):
            if r == tr and c == tc:
                return +(todo == 0)

            ans = 0
            for nr, nc in neighbors(r, c):
                if todo & code(nr, nc):
                    ans += dp(nr, nc, todo ^ code(nr, nc))
            return ans

        return dp(sr, sc, target)
# 39/39 cases passed (64 ms)
# Your runtime beats 65.87 % of python3 submissions
# Your memory usage beats 7.69 % of python3 submissions (13.7 MB)
# @lc code=end
