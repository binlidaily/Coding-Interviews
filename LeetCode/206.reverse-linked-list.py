#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Time: O(n)
# Space: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, node = None, head
        if not node:
            return pre
        while node.next:
            next = node.next
            node.next = pre
            pre = node
            node = next
        node.next = pre
        return node

    def reverseList1(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
# 27/27 cases passed (32 ms)
# Your runtime beats 81.2 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14 MB)

# 2. Recursioin
# Time: O(n)
# Space: O(n)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self._reverse(head)

    def _reverse(self, node, pre=None):
        if not node:
            return pre
        next = node.next
        node.next = pre
        return self._reverse(next, node)

# 27/27 cases passed (32 ms)
# Your runtime beats 81.31 % of python3 submissions
# Your memory usage beats 22.73 % of python3 submissions (18.6 MB)
# @lc code=end
