#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] + [0] * (rowIndex)
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                res[j] = res[j] + res[j-1]
        return res

# 34/34 cases passed (24 ms)
# Your runtime beats 90.08 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().getRow(3))