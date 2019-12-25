#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        if not A or not B or len(A) != len(B):
            return False
        return B in A + A
# 45/45 cases passed (24 ms)
# Your runtime beats 93.96 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

