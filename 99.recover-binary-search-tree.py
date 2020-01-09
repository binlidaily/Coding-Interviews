#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Time Complexity: O(n)
# Space Complexity: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def recoverTree(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         if not root:
#             return None
#         one, two = self.find_two_nodes(root)
#         print(one, two)
#         stack = []
#         node = root
#         while node or stack:
#             while node:
#                 stack.append(node)
#                 node = node.left
#             node = stack.pop()
#             if node.val == one:
#                 node.val = two
#             elif node.val == two:
#                 node.val = one
#             node = node.right
#         # return root

#     def find_two_nodes(self, root):
#         if not root:
#             return None, None
#         stack = []        
#         res = []
#         node = root
#         while stack or node:
#             while node:
#                 stack.append(node)
#                 node = node.left
#             node = stack.pop()
#             res.append(node.val)
#             node = node.right
#         n = len(res)
#         max_val, min_val = None, None
#         for i in range(1, n):
#             if res[i - 1] > res[i]:
#                 if min_val is not None:
#                     min_val = res[i]
#                 else:
#                     max_val, min_val = res[i - 1], res[i]
#         return max_val, min_val

# 1917/1917 cases passed (80 ms)
# Your runtime beats 15.52 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)


# 2. inorder-two array
# Time: O(n)
# Space: O(n)
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        vals, nodes = [], []
        self.inorder(root, vals, nodes)
        vals.sort()
        n = len(vals)
        for i in range(n):
            nodes[i].val = vals[i]

    def inorder(self, root, vals, nodes):
        if not root:
            return
        self.inorder(root.left, vals, nodes)
        vals.append(root.val)
        nodes.append(root)
        self.inorder(root.right, vals, nodes)

# @lc code=end

