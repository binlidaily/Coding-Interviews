#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        res = []
        n = len(strs[0])
        for i in range(n):
            cur = strs[0][i]
            for s in strs:
                if i >= len(s) or cur != s[i]:
                    return ''.join(res)
            res.append(cur)
        return ''.join(res)

# 118/118 cases passed (44 ms)
# Your runtime beats 14.71 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13 MB)
# @lc code=end

print(Solution().longestCommonPrefix(["flower","flow","flight"]))   # 'fl'
print(Solution().longestCommonPrefix(["dog","racecar","car"]))   # ''
print(Solution().longestCommonPrefix(["aa","a"]))   # ''