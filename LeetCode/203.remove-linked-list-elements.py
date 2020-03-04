#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# Time: O(n)
# Space: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        while head and head.val == val:
            head = head.next
        node = head
        while node and node.next:
            if node.next.val == val:
                if node.next.next:
                    node.next = node.next.next
                    continue
                else:
                    node.next = None
                    break
            node = node.next
        return head
# 65/65 cases passed (68 ms)
# Your runtime beats 75.52 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (15.5 MB)
# @lc code=end

