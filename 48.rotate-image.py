#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # return matrix

# 21/21 cases passed (20 ms)
# Your runtime beats 99.73 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))