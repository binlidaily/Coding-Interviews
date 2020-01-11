#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)
# Runtime: 32 ms, faster than 65.80%
# Memory Usage: 12.8 MB, less than 100.00%
# @lc code=end

print(Solution().findTheDifference(s = "abcd", t = "abcde"))  # e