#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
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
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast, slow = head, head
        while fast and slow:
            if fast.next:
                fast = fast.next.next
            else:
                return None
            slow = slow.next
            if fast == slow:
                break
        
        if not fast or not slow:
            return None
        
        restart = head
        while restart != slow:
            restart = restart.next
            slow = slow.next
        return slow
# 16/16 cases passed (52 ms)
# Your runtime beats 81.56 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (15.9 MB)

# @lc code=end

