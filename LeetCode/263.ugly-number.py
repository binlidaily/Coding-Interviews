#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (41.22%)
# Likes:    355
# Dislikes: 548
# Total Accepted:    186.4K
# Total Submissions: 452.1K
# Testcase Example:  '6'
#
# Write a program to check whether a given number is an ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# 
# Example 1:
# 
# 
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# 
# Example 2:
# 
# 
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# 
# 
# Example 3:
# 
# 
# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.
# 
# 
# Note:
# 
# 
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# 
#

# @lc code=start
# Time: O(n)
# Space: O(1)
# class Solution:
#     def isUgly(self, num: int) -> bool:
#         if num <= 0:
#             return False
        
#         for d in [2, 3, 5]:
#             while num % d == 0:
#                 num /= d
#         return True if num == 1 else False

# 1012/1012 cases passed (32 ms)
# Your runtime beats 46.09 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# 2. Recurrence
# Time: O(n)
# Space: O(1)
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        if num % 2 == 0:
            return self.isUgly(num / 2)
        if num % 3 == 0:
            return self.isUgly(num / 3)
        if num % 5 == 0:
            return self.isUgly(num / 5)
        return False

# 1012/1012 cases passed (28 ms)
# Your runtime beats 76.39 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().isUgly(6))
print(Solution().isUgly(8))
print(Solution().isUgly(14))