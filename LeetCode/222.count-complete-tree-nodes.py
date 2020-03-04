#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
import collections
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
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left, right = root, root
        height = 0
        while right:
            left = left.left
            right = right.right
            height += 1
        if not left:
            return (1 << height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# 18/18 cases passed (68 ms)
# Your runtime beats 97.54 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (20 MB)


# Time: O(nlogn)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         queue = collections.deque()
#         queue.append(root)
#         cnt = 0
#         while queue:
#             size = len(queue)
#             cnt += size
#             for _ in range(size):
#                 node = queue.popleft()
#                 if not node:
#                     continue
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return cnt
                
# 18/18 cases passed (92 ms)
# Your runtime beats 39.51 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (20 MB)
# @lc code=end

