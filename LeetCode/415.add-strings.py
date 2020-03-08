#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (46.04%)
# Likes:    701
# Dislikes: 215
# Total Accepted:    147.6K
# Total Submissions: 320.3K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return num2 or num1
        str_int = dict(zip(list('0123456789')+['10', '11', '12', '13', '14', '15', '16', '17', '18'], range(19)))
        int_str = dict(zip(range(19), list('0123456789')+['10', '11', '12', '13', '14', '15', '16', '17', '18']))
        n1, n2 = len(num1), len(num2)
        res = ['0'] * (max(n1, n2) + 1)
        n = len(res)
        
        for i in range(n):
            add = str_int[res[n - i - 1]] \
                + (str_int[num1[n1 - i - 1]] if n1 - i - 1 >= 0 else 0) \
                + (str_int[num2[n2 - i - 1]] if n2 - i - 1 >= 0 else 0)
            res[n - i - 1] = int_str[add % 10]
            res[n - i - 2] = int_str[str_int[res[n - i - 2]] + add // 10]

        for i in range(n):
            if res[i] != '0' or i == n-1:
                return ''.join(res[i:])
        return ''

# 315/315 cases passed (104 ms)
# Your runtime beats 12.07 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)


# @lc code=end

print(Solution().addStrings('1', '2'), '3')
print(Solution().addStrings('88', '22'), '110')
print(Solution().addStrings('9', '99'), '108')