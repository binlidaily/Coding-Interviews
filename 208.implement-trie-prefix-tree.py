#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
import collections
# @lc code=start
# Time: O(n)
# Space: O(n)

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
            # only this one line can work
            # cur = cur.children[letter]
        cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for letter in word:
            cur = cur.children.get(letter)
            if not cur:
                return False
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for letter in prefix:
            cur = cur.children.get(letter)
            if not cur:
                return False
        return True

# 15/15 cases passed (188 ms)
# Your runtime beats 53.64 % of python3 submissions
# Your memory usage beats 7.41 % of python3 submissions (31.5 MB)
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

trie = Trie()

trie.insert("apple")
print(trie.search("apple"))   # returns true
print(trie.search("app"))     # returns false
print(trie.startsWith("app")) # returns true
trie.insert("app");   
print(trie.search("app"))     # returns true