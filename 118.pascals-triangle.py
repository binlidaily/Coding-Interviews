#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        res = []
        for i in range(numRows):
            row = []
            for j in range(i):
                if j == 0:
                    row.append(1)
                else:
                    row.append(res[-1][j-1] + res[-1][j])
            row.append(1)
            res.append(row)
        return res

# 15/15 cases passed (24 ms)
# Your runtime beats 88.09 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().generate(5))