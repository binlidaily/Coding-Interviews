#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        sign = '+'
        val = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                val = val * 10 + int(ch)
            if (not ch.isdigit() and ch != ' ') or len(s) - 1== i:
                if sign == '+':
                    stack.append(val)
                elif sign == '-':
                    stack.append(-val)
                elif sign == '/':
                    if stack[-1] > 0:
                        stack.append(stack.pop() // val)
                    else:
                        stack.append(int(stack.pop() / val))
                elif sign == '*':
                    stack.append(stack.pop() * val)
                sign = ch
                val = 0
        for num in stack:
            res += num
        return res

# 109/109 cases passed (96 ms)
# Your runtime beats 62.52 % of python3 submissions
# Your memory usage beats 88.89 % of python3 submissions (14.4 MB)
# @lc code=end

print(Solution().calculate("1 + 1"))    # 2
print(Solution().calculate(" 2-1 + 2 "))    # 3
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))    # 23
print(Solution().calculate("14-3/2"))    # 13