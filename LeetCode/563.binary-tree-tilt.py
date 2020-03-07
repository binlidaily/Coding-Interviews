#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#
# https://leetcode.com/problems/binary-tree-tilt/description/
#
# algorithms
# Easy (47.74%)
# Likes:    422
# Dislikes: 1024
# Total Accepted:    67.1K
# Total Submissions: 140.5K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree, return the tilt of the whole tree.
# 
# The tilt of a tree node is defined as the absolute difference between the sum
# of all left subtree node values and the sum of all right subtree node values.
# Null node has tilt 0.
# 
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
# 
# Example:
# 
# Input: 
# ⁠        1
# ⁠      /   \
# ⁠     2     3
# Output: 1
# Explanation: 
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# 
# 
# 
# Note:
# 
# The sum of node values in any subtree won't exceed the range of 32-bit
# integer. 
# All the tilt values won't exceed the range of 32-bit integer.
# 
# 
#

# @lc code=start
# Time: O(nlogn)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        return abs(self.nodeSum(root.left) - self.nodeSum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
    
    def nodeSum(self, root):
        if not root:
            return 0
        return self.nodeSum(root.left) + self.nodeSum(root.right) + root.val

# 75/75 cases passed (596 ms)
# Your runtime beats 7.44 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.4 MB)
# @lc code=end

