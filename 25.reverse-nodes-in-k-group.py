#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 2:
            return head
    
        next_head = head
        for i in range(k - 1):
            next_head = next_head.next
            if next_head is None:
                return head
        ret = next_head

        current = head
        while next_head:
            tail = current
            prev = None
            for i in range(k):
                if next_head:
                    next_head = next_head.next
                _next = current.next
                current.next = prev
                prev = current
                current = _next
            tail.next = next_head or current

        return ret
# 81/81 cases passed (44 ms)
# Your runtime beats 89.73 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.8 MB)
# @lc code=end

