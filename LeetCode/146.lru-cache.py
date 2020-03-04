#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
# Time: O(1)
# Space: O(n)

class ListNode():
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None

class DoubleLinkedNode():
    def __init__(self):
        self.header = None
        self.tail = None

    def add_head(self, node):
        if not self.header:
            self.header = node
            self.tail = node
        else:
            header = self.header
            self.header = node
            node.next = header
            header.pre = node

    def remove(self, node):
        pre, next = node.pre, node.next
        if pre:
            pre.next = next
        else:
            self.header = next
        
        if next:
            next.pre = pre
        else:
            self.tail = pre
        
        node.pre = None
        node.next = None
        # del node

    def remove_last(self):
        if not self.tail:
            return None
        tail = self.tail
        self.remove(tail)
        return tail

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.size = 0
        self.linkedlist = DoubleLinkedNode()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.linkedlist.remove(node)
        self.linkedlist.add_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.size += 1
            node = ListNode(key, value)
            self.cache[key] = node
            self.linkedlist.add_head(node)
        else:
            node = self.cache[key]
            node.val = value
            self.linkedlist.remove(node)
            self.linkedlist.add_head(node)

        if self.size > self.capacity:
            self.size -= 1
            tail = self.linkedlist.remove_last()
            del self.cache[tail.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 18/18 cases passed (208 ms)
# Your runtime beats 64.76 % of python3 submissions
# Your memory usage beats 6.06 % of python3 submissions (22.5 MB)
# @lc code=end

