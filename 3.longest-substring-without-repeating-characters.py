#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
import collections
# @lc code=start
# Time: O(n)
# Space: o(n)
class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        start = 0
        res = 0
        hash_table = collections.defaultdict(int)
        for i in range(n):
            if s[i] in hash_table:
                start = max(start, hash_table[s[i]]+1)
            res = max(res, i-start+1)
            hash_table[s[i]] = i
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        n = len(s)
        visited = set()
        res = 0
        while l < n and r < n:
            if s[r] in visited:
                if s[l] in visited:
                    visited.remove(s[l])
                l += 1
            else:
                res = max(res, r-l+1)
                visited.add(s[r])
                r += 1
        return res

# @lc code=end

