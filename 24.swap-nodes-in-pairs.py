#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 1. Recursion
# Time: O(n)
# Space: O(1)
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         first, second = head, head.next
#         head = second.next
#         second.next = first
#         first.next = self.swapPairs(head)
#         return second

# 55/55 cases passed (24 ms)
# Your runtime beats 91.6 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# 2. Iterative
# Time: O(n)
# Space: O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            first, second = head.next, head.next.next
            first.next = second.next
            second.next = first
            head.next = second
            head = first
        return dummy.next

# 55/55 cases passed (24 ms)
# Your runtime beats 91.6 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

ls1 = ListNode(1)
ls2 = ListNode(2)
ls3 = ListNode(3)
ls4 = ListNode(4)
ls1.next = ls2
ls2.next = ls3
ls3.next = ls4

def output(ls):
    while ls:
        print(ls.val)
        ls = ls.next
output(ls1)
print('-'*10)
output(Solution().swapPairs(ls1))