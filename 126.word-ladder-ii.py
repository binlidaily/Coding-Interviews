#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
import string
from typing import List
import collections
# @lc code=start
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         res = []
#         self.alpha = string.ascii_lowercase # a-z
#         self.min = float('inf')
#         visited = set()
#         visited.add(beginWord)
#         self.dfs(endWord, set(wordList), visited, beginWord, [beginWord], res)
#         min_len = self.find_min_len(res)
#         return [path for path in res if len(path) == min_len]
    
#     def find_min_len(self, res):
#         min_len = float('inf')
#         for path in res:
#             size = len(path)
#             if size < min_len:
#                 min_len = size
#         return min_len

#     def dfs(self, endWord, wordList, visited, word, path, res):
#         if word == endWord:
#             size = len(path)
#             if size <= self.min:
#                 self.min = size
#                 res.append(path)
#             return

#         if len(path) > self.min:
#             return

#         n = len(word)
#         for i in range(n):
#             for ch in self.alpha:
#                 new_word = word[:i] + ch + word[i+1:]
#                 if new_word in wordList and new_word not in visited:
#                     visited.add(new_word)
#                     self.dfs(endWord, wordList, visited, new_word, path+[new_word], res)
#                     visited.remove(new_word)
# TLE

# 2. BFS
# Time: O()
# Space: O()
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        all_adj_combine = collections.defaultdict(list)
        wordLen = len(beginWord)
        for w in wordList:
            for i in range(wordLen):
                all_adj_combine[w[:i] + "*" + w[i + 1:]].append(w)
        level = {}
        for w in wordList:
            level[w] = float("inf")
        level[beginWord] = 0
            
        # BFS
        res = []
        size = float("inf")
        queue = [(beginWord, [beginWord])]
        while queue:
            word, path_list = queue.pop(0)
            if len(path_list) >= size:
                return res
            for i in range(wordLen):
                adj_words = all_adj_combine[word[:i] + "*" + word[i + 1:]]
                for adj_w in adj_words:
                    if adj_w == endWord:
                        res.append(path_list + [adj_w])
                        size = len(path_list + [adj_w])
                    elif level[adj_w] > level[word]:
                        queue.append((adj_w, path_list + [adj_w]))
                        level[adj_w] = level[word] + 1
        return res
# Runtime: 348 ms, faster than 71.55%
# Memory Usage: 17.7 MB, less than 8.33%

            
# @lc code=end

print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution().findLadders("a", "c", ["a","b","c"]))
print(Solution().findLadders("kiss", "tusk", ["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]))
