#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#
import collections
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
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = collections.deque()
        queue.append(root)
        is_1st_none = False
        while queue:
            node = queue.popleft()
            if not node:
                is_1st_none = True
            else:
                if is_1st_none:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True
# 119/119 cases passed (28 ms)
# Your runtime beats 93.74 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

