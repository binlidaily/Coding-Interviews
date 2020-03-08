#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (32.92%)
# Likes:    1077
# Dislikes: 1705
# Total Accepted:    487.5K
# Total Submissions: 1.5M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#

# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            x_cmp = mid ** 2
            if x_cmp == x:
                return mid
            elif x_cmp > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

# 1017/1017 cases passed (28 ms)
# Your runtime beats 90.13 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)

class Solution1:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            center = x / mid
            if mid == center:
                return mid
            elif mid > center:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
# @lc code=end

print(Solution().mySqrt(4), 2)
print(Solution().mySqrt(8), 2)