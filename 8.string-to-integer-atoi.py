#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def myAtoi(self, str: str) -> int:
        if not str or str == '':
            return 0
        chars = 'abcdefghijklmnopqrstuvwxyz'
        keys = list('0123456789')
        values = range(10)
        chardic = dict(zip(keys, values))
        strlst = list(str)
        digit = []
        for ch in strlst:
            if not digit and (ch in chars or ch == '.'):
                return 0
            if not digit and (ch == '+' or ch == '-' or ch.isdigit()):
                digit.append(ch)
            elif digit and ch.isdigit():
                digit.append(ch)
            elif digit and not ch.isdigit():
                break
        res = 0
        if not digit:
            return 0
        sign = -1 if digit[0] == '-' else 1
        for d in digit:
            if d == '-' or d == '+':
                continue
            elif not res:
                res = chardic[d]
            else:
                res = res * 10 + chardic[d]
        res = res * sign
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        elif res < -2 ** 31:
            res = -2 ** 31
        return res

# 1079/1079 cases passed (48 ms)
# Your runtime beats 8.94 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().myAtoi('42'))  # 42
print(Solution().myAtoi("   -42"))  # -42
print(Solution().myAtoi('4193 with words'))  # 4193
print(Solution().myAtoi('words and 987'))  # 0
print(Solution().myAtoi('-91283472332'))  # -2147483648
print(Solution().myAtoi("3.14159"))  # 3
print(Solution().myAtoi(".1"))  # 0
print(Solution().myAtoi("+"))  # 0
print(Solution().myAtoi("+1"))  # 1
print(Solution().myAtoi("  0000000000012345678"))  # 12345678
print(Solution().myAtoi("  "))  # 12345678