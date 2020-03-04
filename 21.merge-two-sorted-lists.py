#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         node = dummy
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 node.next = l1
#                 l1 = l1.next
#             else:
#                 node.next = l2
#                 l2 = l2.next
#             node = node.next
#         if l1:
#             node.next = l1
#         if l2:
#             node.next = l2
#         return dummy.next

# 208/208 cases passed (32 ms)
# Your runtime beats 85.62 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)


# Time: O(n)
# Space: O(121)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l2 or l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# 208/208 cases passed (36 ms)
# Your runtime beats 62.62 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=end

