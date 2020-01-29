#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
from typing import List
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def findMode(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         stack = []
#         node = root
#         hash_map = {}
#         max_val = float('-inf')
#         res = []
#         while node or stack:
#             while node:
#                 stack.append(node)
#                 node = node.left
#             node = stack.pop()
#             hash_map[node.val] = hash_map.get(node.val, 0) + 1
#             max_val = max(hash_map[node.val], max_val)
#             node = node.right
#         for key, value in hash_map.items():
#             if value == max_val:
#                 res.append(key)
#         return res

# 25/25 cases passed (56 ms)
# Your runtime beats 65.56 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (16.6 MB)


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, prev, cnt, max_cnt, result):
            if not root:
                return prev, cnt, max_cnt

            prev, cnt, max_cnt = inorder(root.left, prev, cnt, max_cnt, result)
            if prev:
                if root.val == prev.val:
                    cnt += 1
                else:
                    cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt
                del result[:]
                result.append(root.val)
            elif cnt == max_cnt:
                result.append(root.val)
            return inorder(root.right, root, cnt, max_cnt, result)

        if not root:
            return []
        result = []
        inorder(root, None, 1, 0, result)
        return result
# 25/25 cases passed (60 ms)
# Your runtime beats 39.26 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (16.5 MB)
# @lc code=end

