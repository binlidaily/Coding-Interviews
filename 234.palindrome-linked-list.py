#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        array = []
        node = head
        while node:
            array.append(node.val)
            node = node.next
        l, r = 0, len(array)-1
        while l <= r:
            if array[l] != array[r]:
                return False
            l += 1
            r -= 1
        return True
# 26/26 cases passed (76 ms)
# Your runtime beats 54.24 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (22.8 MB)
# @lc code=end

