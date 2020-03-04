#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# DFS-Recursion
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return None
#         root.right, root.left = root.left, root.right

#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root
# 68/68 cases passed (28 ms)
# Your runtime beats 67.73 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# DFS-Recursion 2
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return None
#         left, right = root.left, root.right

#         root.right = self.invertTree(left)
#         root.left = self.invertTree(right)
#         return root
# 68/68 cases passed (28 ms)
# Your runtime beats 67.8 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)


# DFS-Recursion 3
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root

# 68/68 cases passed (24 ms)
# Your runtime beats 89.08 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# DFS-Iterative
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return None
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             node.right, node.left = node.left, node.right
#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
#         return root

# 68/68 cases passed (20 ms)
# Your runtime beats 97.49 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)

# BFS-Recursion
# import collections
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return None
#         queue = collections.deque()
#         queue.append(root)
#         while queue:
#             node = queue.popleft()
#             node.right, node.left = node.left, node.right
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         return root

# 68/68 cases passed (24 ms)
# Your runtime beats 89.08 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

