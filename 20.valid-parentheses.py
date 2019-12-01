#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        valid=dict(zip([')',"]","}"],["(","[","{"]))
        s=list(s)
        stack=list()
        for i in range(len(s)):
            if s[i] in valid.values():
                stack.append(s[i])
            elif stack==[] or valid[s[i]]!=stack.pop():
                return False
        return not stack
# 76/76 cases passed (28 ms)
# Your runtime beats 92.12 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=end

print(Solution().isValid("(])"))