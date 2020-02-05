#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
import collections
# @lc code=start
# Time: O(n)
# Space: O(2n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (not s and t) or (s and not s) or len(s) != len(t):
            return False
        n = len(s)
        hash_s = collections.defaultdict()
        hash_t = collections.defaultdict()
        for i in range(n):
            if s[i] in hash_s:
                if hash_s[s[i]] != t[i]:
                    return False
            else:
                hash_s[s[i]] = t[i]
            if t[i] in hash_t:
                if hash_t[t[i]] != s[i]:
                    return False
            else:
                hash_t[t[i]] = s[i]
        return True
# 30/30 cases passed (40 ms)
# Your runtime beats 57.07 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# @lc code=end

print(Solution().isIsomorphic(s = "egg", t = "add"))    # True
print(Solution().isIsomorphic(s = "", t = ""))  # True
print(Solution().isIsomorphic(s = "ab", t = "aa"))  # False