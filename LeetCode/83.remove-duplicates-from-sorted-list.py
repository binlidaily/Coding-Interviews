#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node:
            if node.next and node.next.val == node.val:
                node.next = node.next.next
                continue
            node = node.next
        return head

# 165/165 cases passed (32 ms)
# Your runtime beats 97.89 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=end

a = ListNode(1)
b = ListNode(1)
c = ListNode(1)

a.next = b
b.next = c

def output(node):
    while node:
        print(node.val)
        node = node.next

output(Solution().deleteDuplicates(a))