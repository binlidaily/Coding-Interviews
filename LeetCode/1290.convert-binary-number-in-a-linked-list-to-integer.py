#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
#
# algorithms
# Easy (79.89%)
# Likes:    206
# Dislikes: 23
# Total Accepted:    34.6K
# Total Submissions: 43.3K
# Testcase Example:  '[1,0,1]'
#
# Given head which is a reference node to a singly-linked list. The value of
# each node in the linked list is either 0 or 1. The linked list holds the
# binary representation of a number.
# 
# Return the decimal value of the number in the linked list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# 
# 
# Example 2:
# 
# 
# Input: head = [0]
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: head = [1]
# Output: 1
# 
# 
# Example 4:
# 
# 
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880
# 
# 
# Example 5:
# 
# 
# Input: head = [0,0]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
# 
#
import collections
# @lc code=start
# Time: O(n)
# Space: O(n)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def getDecimalValue(self, head: ListNode) -> int:
        queue = collections.deque()
        while head:
            queue.append(head.val)
            head = head.next
        n = len(queue)
        value = 0
        while queue and n > 0:
            n -= 1
            value += queue.popleft() * 2 ** n
        return value

# 102/102 cases passed (28 ms)
# Your runtime beats 69.84 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# one pass
# Time: O(n)
# Space: O(1)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        res = 0
        while node:
            res = res * 2 + node.val
            node = node.next

        return res

# 102/102 cases passed (28 ms)
# Your runtime beats 69.84 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

