#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        less, gt_eq = None, None
        left, right = None, None
        node = head
        while node:
            if node.val < x:
                if not less:
                    left = node
                else:
                    less.next = node
                less = node
            else: # node.val >= x
                if not gt_eq:
                    right = node
                else:
                    gt_eq.next = node
                gt_eq = node
            node = node.next
        if not less or not gt_eq:
            return right or left
        else:
            less.next = right
            gt_eq.next = None
            return left
# 166/166 cases passed (28 ms)
# Your runtime beats 94.34 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)

# @lc code=end

