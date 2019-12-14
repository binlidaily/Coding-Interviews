#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words or len(words) == 0:
            return []
        sets = set(words)
        res = []
        for word in words:
            if self.dfs(word, sets):
                res.append(word)
        return res
    
    def dfs(self, word, words):
        n = len(word)
        for i in range(1, n):
            prefix = word[:i]
            suffix = word[i:]
            
            if prefix in words and suffix in words:
                return True
            
            if prefix in words and self.dfs(suffix, words):
                return True
            
            # if self.dfs(prefix, words) and suffix in words:
            #     return True
        return False
# 44/44 cases passed (404 ms)
# Your runtime beats 78.01 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (15.9 MB)
# @lc code=end

