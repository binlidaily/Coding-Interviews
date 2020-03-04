#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
# Time: O(logn)
# Space: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        res = 1
        while n != 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n >>= 1
        return res
# 304/304 cases passed (28 ms)
# Your runtime beats 65.82 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().myPow(2.0000, 10))