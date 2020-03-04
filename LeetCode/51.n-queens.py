#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0:
            return []
        res = []
        self.dfs(n, [], [], [], res)
        return [['.' * i + 'Q' + (n - i - 1) * '.' for i in sol] for sol in res]
    
    def dfs(self, n, xydiff_diag, xysum_diag, queens, res):
        # q is the current row index, queen store every column position of a queen
        r = len(queens)
        if r == n:
            res.append(queens)
            return
        
        # check every column position, c is the test column index
        for c in range(n):
            if c in queens or r - c in xydiff_diag or r + c in xysum_diag:
                continue
            self.dfs(n, xydiff_diag + [r - c], xysum_diag + [r + c], queens + [c], res)
# 9/9 cases passed (52 ms)
# Your runtime beats 97 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13 MB)

# @lc code=end

