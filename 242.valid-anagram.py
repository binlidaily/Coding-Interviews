#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t or len(s) != len(t):
            return False
        sd = self.to_dict(s)
        td = self.to_dict(t)
        return sd == td
    
    def to_dict(self, s):
        if not s:
            return {}
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        return dic
# 34/34 cases passed (52 ms)
# Your runtime beats 60.73 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.1 MB)


# @lc code=end

