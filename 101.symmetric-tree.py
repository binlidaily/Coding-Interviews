#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Time: O(n)
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         return self.is_mirror(root.left, root.right)
    
#     def is_mirror(self, left, right):
#         if not left or not right:
#             return left == right
#         if left.val != right.val:
#             return False
#         return self.is_mirror(left.left, right.right) and \
#             self.is_mirror(left.right, right.left)

# 195/195 cases passed (32 ms)
# Your runtime beats 69.89 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)

# 2. Iterative-stack
# Time: O(n)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         left_stack, right_stack = [root.left], [root.right]
#         while len(left_stack) > 0 and len(right_stack) > 0:
#             left = left_stack.pop()
#             right = right_stack.pop()
#             if not left and not right:
#                 continue
#             elif not left or not right:
#                 return False
#             if left.val != right.val:
#                 return False
#             left_stack.append(left.left)
#             right_stack.append(right.right)
#             left_stack.append(left.right)
#             right_stack.append(right.left)
#         return len(left_stack) == 0 and len(right_stack) == 0

# 195/195 cases passed (32 ms)
# Your runtime beats 69.89 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)


# 2. Iterative-stack
# Time: O(n)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_queue, right_queue = collections.deque([root.left]), collections.deque([root.right])
        while len(left_queue) > 0 and len(right_queue) > 0:
            left = left_queue.popleft()
            right = right_queue.popleft()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            left_queue.append(left.left)
            right_queue.append(right.right)
            left_queue.append(left.right)
            right_queue.append(right.left)
        return len(left_queue) == 0 and len(right_queue) == 0

# 195/195 cases passed (36 ms)
# Your runtime beats 33.94 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

