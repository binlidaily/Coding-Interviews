#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#
# https://leetcode.com/problems/transpose-matrix/description/
#
# algorithms
# Easy (63.33%)
# Likes:    328
# Dislikes: 276
# Total Accepted:    66.5K
# Total Submissions: 105.1K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix A, return the transpose of A.
# 
# The transpose of a matrix is the matrix flipped over it's main diagonal,
# switching the row and column indices of the matrix.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000
# 
# 
# 
#
from typing import List
# @lc code=start
# Time: O(mn)
# Space: O(n)
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return []
        row, col = len(A), len(A[0])

        res = []
        for c in range(col):
            cols = []
            for r in range(row):
                cols.append(A[r][c])
            res.append(cols)
        return res

# 36/36 cases passed (76 ms)
# Your runtime beats 56.02 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.5 MB)

# @lc code=end

print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]), [[1,4,7],[2,5,8],[3,6,9]])
# print(Solution().transpose([[1,2,3],[4,5,6]]), [[1,4],[2,5],[3,6]])