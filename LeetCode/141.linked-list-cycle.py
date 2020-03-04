#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Time: O(n)
# Space: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        faster, slower = head, head
        while faster and slower:
            if faster.next:
                faster = faster.next.next
            else:
                faster = None
            slower = slower.next
            if faster == slower:
                return True
        return False
# 17/17 cases passed (48 ms)
# Your runtime beats 89.92 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (16 MB)
# @lc code=end

