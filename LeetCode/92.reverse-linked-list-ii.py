#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        # 否则只有一个节点时，会出现问题，没有 next 指针的报错
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, dummy.next
        diff = n - m
        while m > 1:
            pre, cur = cur, cur.next
            m -= 1
        last_unswapped, first_swapped = pre, cur
        while diff >= 0: # pre是结束反转的结点
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next
            diff -= 1
        last_unswapped.next, first_swapped.next = pre, cur
        return dummy.next
# 44/44 cases passed (28 ms)
# Your runtime beats 74.7 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

