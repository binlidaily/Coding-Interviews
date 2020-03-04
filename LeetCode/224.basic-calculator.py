#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
# Time: O(n)
# Space: O(n)
# class Solution:
#     def calculate(self, s: str) -> int:
#         res, val, sign, stack = 0, 0, 1, []
#         for ch in s:
#             if ch.isdigit():
#                 val = 10 * val + int(ch)
#             elif ch in '-+':
#                 res += sign * val
#                 val = 0
#                 sign =[-1, 1][ch == '+']
#             elif ch == '(':
#                 stack.append(res)
#                 stack.append(sign)
#                 sign, res = 1, 0
#             elif ch == ')':
#                 res += sign * val
#                 res *= stack.pop()
#                 res += stack.pop()
#                 val = 0
#         return res + val * sign

# 37/37 cases passed (72 ms)
# Your runtime beats 92.26 % of python3 submissions
# Your memory usage beats 7.14 % of python3 submissions (14.2 MB)

# Time: O(n)
# Space: O(n)
class Solution:
    def calculate(self, s: str) -> int:
        arr = []
        for c in s:
            arr.append(c)
        return self.helper(arr)

    def helper(self, arr):
        stack = []
        sign = '+'
        num = 0
        while len(arr) > 0:
            c = arr.pop(0)
            if c.isdigit():
                num = num*10 + int(c)
            if c == '(':
                num = self.helper(arr)
            if c == '+' or c == '-' or c == ')' or len(arr) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                sign = c
                num = 0
                if c == ')':
                    break
        return sum(stack)

# 37/37 cases passed (4300 ms)
# Your runtime beats 5.1 % of python3 submissions
# Your memory usage beats 7.14 % of python3 submissions (16.4 MB)
# @lc code=end

print(Solution().calculate("1 + 1"))    # 2
print(Solution().calculate(" 2-1 + 2 "))    # 3
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))    # 23