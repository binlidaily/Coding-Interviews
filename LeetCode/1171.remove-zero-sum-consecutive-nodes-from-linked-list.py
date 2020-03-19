#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/
#
# algorithms
# Medium (41.75%)
# Likes:    320
# Dislikes: 25
# Total Accepted:    11.5K
# Total Submissions: 27.6K
# Testcase Example:  '[1,2,-3,3,1]'
#
# Given the head of a linked list, we repeatedly delete consecutive sequences
# of nodes that sum to 0 until there are no such sequences.
# 
# After doing so, return the head of the final linked list.  You may return any
# such answer.
# 
# 
# (Note that in the examples below, all sequences are serializations of
# ListNode objects.)
# 
# Example 1:
# 
# 
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2,3,-3,-2]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.
# 
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
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        sum_hash = collections.defaultdict()
        prefix = 0
        sum_hash[0] = dummy
        node = head
        while node:
            prefix += node.val
            if prefix in sum_hash:
                sum_hash[prefix].next = node.next
                sum_hash.clear()
                node = dummy
                sum_hash[0] = dummy
                prefix = 0
            else:
                sum_hash[prefix] = node
            node = node.next
        return dummy.next

# 105/105 cases passed (52 ms)
# Your runtime beats 24.11 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.3 MB)

# Time: O(n)
# Space: O(n)
class Solution2:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next

# 105/105 cases passed (48 ms)
# Your runtime beats 28.44 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.3 MB)


# Time: O(n)
# Space: O(n)
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        sum_hash = collections.defaultdict()
        while cur:
            prefix += cur.val
            sum_hash[prefix] = cur
            cur = cur.next
        
        cur = dummy
        prefix = 0
        while cur:
            prefix += cur.val
            cur.next = sum_hash[prefix].next
            cur = cur.next
        return dummy.next

# 105/105 cases passed (40 ms)
# Your runtime beats 82.67 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.2 MB)
# @lc code=end

a = ListNode(1)
a1 = ListNode(2)
a2 = ListNode(3)
a3 = ListNode(-3)
a4 = ListNode(-2)

# a = ListNode(1)
# a1 = ListNode(2)
# a2 = ListNode(3)
# a3 = ListNode(-3)
# a4 = ListNode(2)

a.next = a1
a1.next = a2
a2.next = a3
a3.next = a4

def output(head):
    res = []
    while head:
        res.append(head.val) 
        head = head.next
    print(res)

output(a)
output(Solution().removeZeroSumSublists(a))
