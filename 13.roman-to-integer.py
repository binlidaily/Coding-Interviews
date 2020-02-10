#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        _dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        sum = 0
        for i in s[::-1]:
            curr = _dict[i]
            if prev > curr:
                sum -= curr
            else:
                sum += curr
            prev = curr
        return sum
        
# 3999/3999 cases passed (40 ms)
# Your runtime beats 88.02 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

