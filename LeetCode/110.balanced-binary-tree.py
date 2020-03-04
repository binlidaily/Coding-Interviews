#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# Time: O(n)
# Space: O(1)
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        is_flag, height = self._is_balanced(root)
        return True if is_flag else  False
    
    def _is_balanced(self, root):
        # return is_balanced, height
        if not root:
            return True, 0
        
        left_b, left_h = self._is_balanced(root.left)
        right_b, right_h = self._is_balanced(root.right)
        if not left_b or not right_b:
            return False, -1
        else:
            if abs(left_h - right_h) > 1:
                return False, -1
            else:
                return True, max(left_h, right_h) + 1
# 227/227 cases passed (36 ms)
# Your runtime beats 99.66 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (16.4 MB)

# @lc code=end

