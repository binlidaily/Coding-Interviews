#
# @lc app=leetcode id=1003 lang=python3
#
# [1003] Check If Word Is Valid After Substitutions
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def isValid(self, S: str) -> bool:
        if not S:
            return False
        stack = []
        for ch in S:
            if ch == 'c':
                if not stack or stack.pop() != 'b':
                    return False
                if not stack or stack.pop() != 'a':
                    return False
            else:
                stack.append(ch)
        return True if not stack else False

# 78/78 cases passed (44 ms)
# Your runtime beats 77.04 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)

# @lc code=end

print(Solution().isValid('aaa'))