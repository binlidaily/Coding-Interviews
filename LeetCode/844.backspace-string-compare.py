#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (47.23%)
# Likes:    1065
# Dislikes: 62
# Total Accepted:    104.5K
# Total Submissions: 221.4K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings S and T, return if they are equal when both are typed into
# empty text editors. # means a backspace character.
# 
# 
# Example 1:
# 
# 
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# 
# 
# 
# Example 2:
# 
# 
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# 
# 
# 
# Example 3:
# 
# 
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# 
# 
# 
# Example 4:
# 
# 
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# 
# 
# Follow up:
# 
# 
# Can you solve it in O(N) time and O(1) space?
# 
# 
# 
# 
# 
# 
#

# @lc code=start

# Time: O(n)
# Space: O(n)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack, t_stack = [], []
        for s in S:
            if s == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(s)
        for t in T:
            if t == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(t)
        return s_stack == t_stack

# 104/104 cases passed (32 ms)
# Your runtime beats 37.24 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

# print(Solution().backspaceCompare(S = "ab#c", T = "ad#c"), True)
# print(Solution().backspaceCompare(S = "ab##", T = "c#d#"), True)
# print(Solution().backspaceCompare(S = "a##c", T = "#a#c"), True)
# print(Solution().backspaceCompare(S = "a#c", T = "b"), False)
# print(Solution().backspaceCompare("y#fo##f", "y#f#o##f"), True)
