#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            # if not fast.next:
            #     return None
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        if not fast:
            return slow.next
        else:
            slow.next = slow.next.next
        return head

# 208/208 cases passed (32 ms)
# Your runtime beats 58.65 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

a = ListNode(1)
b = ListNode(2)
# c = ListNode(2)
# b = ListNode(2)
# b = ListNode(2)
a.next = b

def cout(head):
    output = ''
    while head:
        output += str(head.val) + ' '
        head = head.next
    print(output)
cout(Solution().removeNthFromEnd(a, 2))