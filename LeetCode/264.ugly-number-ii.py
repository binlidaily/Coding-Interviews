#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (38.72%)
# Likes:    1351
# Dislikes: 81
# Total Accepted:    130.9K
# Total Submissions: 338.3K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        two, three, five = 0, 0, 0
        for i in range(n):
            if i % 3 == 0:
                two += 1
            if
# @lc code=end

