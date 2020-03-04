#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n <= 0:
            return []
        res = [0]
        self.dfs(n, [], [], [], res)
        return res[0]
    
    def dfs(self, n, xydiff_diag, xysum_diag, queens, res):
        # q is the current row index, queen store every column position of a queen
        r = len(queens)
        if r == n:
            res[0] += 1
            return
        
        # check every column position, c is the test column index
        for c in range(n):
            if c in queens or r - c in xydiff_diag or r + c in xysum_diag:
                continue
            self.dfs(n, xydiff_diag + [r - c], xysum_diag + [r + c], queens + [c], res)
# 9/9 cases passed (44 ms)
# Your runtime beats 94.04 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

