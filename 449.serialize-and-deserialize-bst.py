#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#
import collections
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return 'null'
        
        res = []
        self.preorder(root, res)
        return ','.join(res)

    def preorder(self, root, res):
        if not root:
            res.append('null')
            return
        res.append(str(root.val))
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        queue = collections.deque()
        for node in data.split(','):
            if node != 'null':
                queue.append(int(node))
        return self.build_tree(queue, float('-inf'), float('inf'))


    def build_tree(self, queue, min_val, max_val):
        if queue and min_val < queue[0] < max_val:
            node_val = queue.popleft()
            root = TreeNode(node_val)
            root.left = self.build_tree(queue, min_val, node_val)
            root.right = self.build_tree(queue, node_val, max_val)
            return root
        return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# @lc code=end

