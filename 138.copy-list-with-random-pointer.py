#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Time: O(n)
# Space: O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return 
        # copy nodes
        cur = head
        while cur:
            nxt = cur.next
            cur.next = Node(cur.val, cur.next, cur.random)
            cur.next.next = nxt
            cur = nxt
        # copy random pointers
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # separate two parts
        second = cur = head.next
        while cur.next:
            head.next = cur.next
            head = head.next
            cur.next = head.next
            cur = cur.next
        head.next = None
        return second

# 18/18 cases passed (48 ms)
# Your runtime beats 39.22 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.3 MB)
# @lc code=end

