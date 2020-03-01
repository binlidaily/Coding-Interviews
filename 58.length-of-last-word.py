#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        start = None
        for i in range(n - 1, -1, -1):
            if not start and s[i] != ' ':
                start = i
            if start and s[i] == ' ':
                return start - i
        return start + 1 if start is not None else 0

# 59/59 cases passed (16 ms)
# Your runtime beats 99.57 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().lengthOfLastWord("Hello World"))
print(Solution().lengthOfLastWord(" World"))
print(Solution().lengthOfLastWord(" "))
print(Solution().lengthOfLastWord("a"))