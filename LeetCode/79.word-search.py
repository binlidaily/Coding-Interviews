#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import List
# @lc code=start
# Time: O()
# Space: O()
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board) == 0:
            return False
        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                if self.dfs(board, word, r, c, i, j):
                    return True
        return False
    
    def dfs(self, board, remain, r, c, i, j):
        if remain == '':
            return True
        if i < 0 or i >= r or j < 0 or j >= c or board[i][j] != remain[0]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        
        res = self.dfs(board, remain[1:], r, c, i+1, j) or \
                self.dfs(board, remain[1:], r, c, i-1, j) or \
                self.dfs(board, remain[1:], r, c, i, j+1) or \
                self.dfs(board, remain[1:], r, c, i, j-1)
        board[i][j] = tmp
        return res
# Runtime: 356 ms, faster than 69.16% 
# Memory Usage: 13.7 MB, less than 100.00% 


# @lc code=end

print(Solution().exist([["a"]], "a"))