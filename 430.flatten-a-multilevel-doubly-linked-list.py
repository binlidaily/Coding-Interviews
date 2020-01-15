#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
# Time: O(n)
# Space: O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# class Solution:
#     def flatten(self, head: 'Node') -> 'Node':
#         if not head:
#             return head
#         cur = head
#         while cur:
#             # CASE 1: if no child, proceed
#             if not cur.child:
#                 cur = cur.next
#                 continue
#             # CASE 2: got child, find the tail of the child and link it to cur.next
#             tmp = cur.child
#             # find the tail of the child
#             while tmp.next:
#                 tmp = tmp.next
#             # connect tail with cur.next, if it is not None
#             tmp.next = cur.next
#             if cur.next:
#                 cur.next.prev = tmp
#             cur.next = cur.child
#             cur.child.prev = cur
#             cur.child = None
#         return head
# 22/22 cases passed (36 ms)
# Your runtime beats 72.4 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)


# 2. Stack
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        stack = [head]
        prev = Node(0)
        while stack:
            node = stack.pop()
            node.prev = prev
            prev.next = node
            prev = node
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None
        head.prev = None
        return head
# 22/22 cases passed (32 ms)
# Your runtime beats 87.74 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

