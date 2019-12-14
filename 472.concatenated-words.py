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
# Runtime: 388 ms, faster than 82.71%
# Memory Usage: 16 MB, less than 75.00%
# @lc code=end

