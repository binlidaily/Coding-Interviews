#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
import collections
# @lc code=start
# Time: O(n)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if not node:
                res.append('null')
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        n = len(nodes)
        queue = collections.deque()
        root = TreeNode(int(nodes[0]))
        queue.append(root)
        i = 1
        while i < n:
            parent = queue.popleft()
            if nodes[i] != 'null':
                left = TreeNode(int(nodes[i]))
                parent.left = left
                queue.append(left)
            
            i += 1
            if nodes[i] != 'null':
                right = TreeNode(int(nodes[i]))
                parent.right = right
                queue.append(right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# 48/48 cases passed (116 ms)
# Your runtime beats 56.73 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (17.7 MB)
# @lc code=end

