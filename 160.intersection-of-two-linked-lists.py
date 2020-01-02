#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        size_a, size_b = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            size_a += 1
            nodeA = nodeA.next
        while nodeB:
            size_b += 1
            nodeB = nodeB.next
        nodeA, nodeB = headA, headB
        if size_a == size_b:
            pass
        elif size_a > size_b:
            steps = size_a - size_b
            for _ in range(steps):
                nodeA = nodeA.next
        else:
            steps = size_b - size_a
            for _ in range(steps):
                nodeB = nodeB.next
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None
# 45/45 cases passed (168 ms)
# Your runtime beats 57.54 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (27.8 MB)
# @lc code=end

