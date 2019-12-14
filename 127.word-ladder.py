#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
import string
from typing import List
import collections
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        visited = set()
        queue = collections.deque([(beginWord, 1)])
        alpha = string.ascii_lowercase # 'abcd...z'
        while queue:
            word, length = queue.popleft()
            
            if word == endWord:
                return length
            n = len(word)
            for i in range(n):
                for ch in alpha:
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in wordList and newWord not in visited:
                        queue.append((newWord, length+1))
                        visited.add(newWord)
        return 0
# @lc code=end

