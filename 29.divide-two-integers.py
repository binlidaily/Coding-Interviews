#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sigal = (dividend < 0) == (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            shift = 0
            while dividend >= divisor << shift:
                shift += 1
            res += (1 << (shift - 1))
            dividend -= (divisor << (shift - 1))
        return min(res if sigal else -res, 2147483647)
# 989/989 cases passed (32 ms)
# Your runtime beats 56.52 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
# @lc code=end

print(Solution().divide(10, 3))