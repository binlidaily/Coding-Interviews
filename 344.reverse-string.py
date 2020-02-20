#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        # return s

# 478/478 cases passed (200 ms)
# Your runtime beats 97.93 % of python3 submissions
# Your memory usage beats 98.84 % of python3 submissions (17.2 MB)
# @lc code=end

print(Solution().reverseString(["h","e","l","l","o"]))
print(Solution().reverseString(["H","a","n","n","a","h"]))