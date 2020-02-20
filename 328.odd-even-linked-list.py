#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd, even = ListNode(0), ListNode(0)
        odd_head, even_head = odd, even
        idx = 0
        while head:
            if idx & 1 == 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            idx += 1
        even.next = None
        odd.next = even_head.next
        return odd_head.next

# 71/71 cases passed (44 ms)
# Your runtime beats 51.11 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.6 MB)
# @lc code=end

