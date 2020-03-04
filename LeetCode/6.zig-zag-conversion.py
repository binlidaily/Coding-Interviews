#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        interval = 2 * (numRows - 1)
        res = ''
        # first row
        for i in range(0, n, interval):
            res += s[i]
        # middle lines
        for r in range(1, numRows - 1):
            inter = 2 * r
            i = r
            while i < n:
                res += s[i]
                inter = interval - inter
                i += inter
            
        for i in range(numRows-1, n, interval):
            res += s[i]
        return res

# 1158/1158 cases passed (52 ms)
# Your runtime beats 86.83 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().convert("PAYPALISHIRING", 4))