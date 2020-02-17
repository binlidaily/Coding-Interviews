#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Time: O(logn)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder = []
        node = root
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            inorder.append(node.val)
            if len(inorder) >= k:
                return inorder[-1]
            node = node.right
        return -1

# 91/91 cases passed (48 ms)
# Your runtime beats 80.57 % of python3 submissions
# Your memory usage beats 98.18 % of python3 submissions (16.8 MB)
# @lc code=end

