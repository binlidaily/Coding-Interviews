#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#
from typing import List
import collections
# @lc code=start
# Time: O(n)
# Space: O(nlogn)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []
        row = self.get_height(root)
        col = 2 ** row - 1
        res = [['' for _ in range(col)] for _ in range(row)]
        self.update_output(root, 0, 0, col-1, res)
        return res

    def get_height(self, root):
        if not root:
            return 0
        return 1+ max(self.get_height(root.left), self.get_height(root.right))

    def update_output(self, root, row, left, right, res):
        if not root:
            return
        mid = (left + right) >> 1
        res[row][mid] = str(root.val)
        self.update_output(root.left, row + 1, left, mid - 1, res)
        self.update_output(root.right, row + 1, mid + 1, right, res)
# 73/73 cases passed (36 ms)
# Your runtime beats 33.22 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=end

