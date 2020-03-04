#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
from typing import List
# @lc code=start
# Time: O()
# Space: O()
class Solution:
    def dfs_Sudoku(self, row_map, col_map, sec_map, unfilled, board):
        
        if len(unfilled)==0: return True
        
        row, col = unfilled.pop()
        for num in range(9):
            sec_index = 3 * (row // 3) + col // 3
            if row_map[row][num] == False and \
               col_map[col][num] == False and \
               sec_map[sec_index][num] == False:
                row_map[row][num] = True
                col_map[col][num] = True
                sec_map[sec_index][num] = True
                board[row][col] = str(num+1)
                
                completed = self.dfs_Sudoku(row_map, col_map, sec_map, unfilled, board)
                
                if completed: return True
                
                row_map[row][num] = False
                col_map[col][num] = False
                sec_map[sec_index][num] = False
                board[row][col] = '.'
        unfilled.append((row, col))
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        unfilled = []
        row_map = [[False]*9 for _ in range(9)]
        col_map = [[False]*9 for _ in range(9)]
        sec_map = [[False]*9 for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': 
                    unfilled.append((i,j))
                    continue
                index = int(board[i][j]) - 1
                row_map[i][index] = True
                col_map[j][index] = True
                sec_index = 3 * (i // 3) + j // 3
                sec_map[sec_index][index] = True
        
        self.dfs_Sudoku(row_map, col_map, sec_map, unfilled, board)
# 6/6 cases passed (148 ms)
# Your runtime beats 73.69 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# @lc code=end

