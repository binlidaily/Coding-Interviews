#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Time: O(n)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_path = [0]
        self.find_max_path(root, max_path)
        return max_path[0]
        
    
    def find_max_path(self, root, max_path):
        if not root:
            return 0
        
        left = self.find_max_path(root.left, max_path)
        right = self.find_max_path(root.right, max_path)
        max_path[0] = max(max_path[0], left + right)

        return max(left, right) + 1
# 106/106 cases passed (44 ms)
# Your runtime beats 62.34 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.4 MB)

# @lc code=end

