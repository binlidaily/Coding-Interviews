#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
from typing import List
# @lc code=start
# Time(mn)
# Space(1)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 

        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                cnt = 0
                for x in range(max(0, i - 1), min(i + 2, r)):
                    for y in range(max(0, j - 1), min(j + 2, c)):
                        if (x, y) != (i, j) and 1 <= board[x][y] <= 2:
                            cnt += 1
                if board[i][j] == 0:
                    if cnt == 3:
                        board[i][j] = 3
                else:
                    if cnt < 2 or cnt > 3:
                        board[i][j] = 2

        for i in range(r):
            for j in range(c):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
        # return board
# 23/23 cases passed (20 ms)
# Your runtime beats 99.7 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
print([[0,0,0],[1,0,1],[0,1,1],[0,1,0]])