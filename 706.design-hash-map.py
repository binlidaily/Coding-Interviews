#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self, size=None):
        """
        Initialize your data structure here.
        """
        if not size:
            self.size = 1000
        else:
            self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = self._hash_function(key)
        for item in self.table[hash_key]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_key].append(Item(key, value))


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = self._hash_function(key)
        for item in self.table[hash_key]:
            if item.key == key:
                return item.value
        # raise KeyError('Key Not Found')
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = self._hash_function(key)
        for index, item in enumerate(self.table[hash_key]):
            if item.key == key:
                del self.table[hash_key][index]
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# 33/33 cases passed (228 ms)
# Your runtime beats 68.13 % of python3 submissions
# Your memory usage beats 63.64 % of python3 submissions (15.7 MB)
# @lc code=end

