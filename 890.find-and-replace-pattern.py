#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        n = len(pattern)
        for item in words:
            dic = {}
            Flag = True
            for i in range(n):
                if pattern[i] in dic:
                    if item[i] != dic[pattern[i]]:
                        Flag = False
                        break
                else:
                    if item[i] in dic.values():
                        Flag = False
                        break
                    dic[pattern[i]] = item[i]
            if Flag:
                res.append(item)
        return res
# 46/46 cases passed (32 ms)
# Your runtime beats 79 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

