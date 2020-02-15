#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = set({'+', '-', '*', '/'})
        res = None
        if len(tokens) == 1:
            return int(tokens[0])

        for ch in tokens:
            if stack and ch in operand:
                second = int(stack.pop())
                if not stack:
                    return None
                first = int(stack.pop())
                if ch == '+':
                    tmp = first + second
                elif ch == '-':
                    tmp = first - second
                elif ch == '*':
                    tmp = first * second
                else:
                    if (first >= 0 and second < 0) or (first <= 0 and second > 0):
                        tmp = abs(first) // abs(second)
                        tmp = -tmp
                    else:
                        tmp = first // second
                res = tmp
                stack.append(tmp)
            else:
                stack.append(ch)
        return res

# 20/20 cases passed (68 ms)
# Your runtime beats 64.81 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().evalRPN(["2", "1", "+", "3", "*"]))    # 9
print(Solution().evalRPN(["4", "13", "5", "/", "+"]))   # 6
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))    # 22
print(Solution().evalRPN(['18']))