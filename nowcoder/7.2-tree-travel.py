# -*- coding:utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeToSequence:
    # def convert(self, root):
    #     res = []
    #     pre = []
    #     self.preorder_recursion(root, pre)
    #     res.append(pre)
    #     ino = []
    #     self.inorder_recursion(root, ino)
    #     res.append(ino)
    #     pos = []
    #     self.postorder_recursion(root, pos)
    #     res.append(pos)
    #     return res
    def convert(self, root):
        # write code here
        res = []
        res.append(self.preorder_iteration(root))
        res.append(self.inorder_iteration(root))
        res.append(self.postorder_iteration2(root))
        return res

    def preorder_recursion(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.preorder_recursion(root.left, res)
        self.preorder_recursion(root.right, res)
    
    def inorder_recursion(self, root, res):
        if not root:
            return
        self.inorder_recursion(root.left, res)
        res.append(root.val)
        self.inorder_recursion(root.right, res) 

    def postorder_recursion(self, root, res):
        if not root:
            return
        self.postorder_recursion(root.left, res)
        self.postorder_recursion(root.right, res)
        res.append(root.val)
    
    def preorder_iteration(self, root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res
    
    def inorder_iteration(self, root):
        if not root:
            return []
        stack = []
        node = root
        res = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    def postorder_iteration1(self, root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return res[::-1]
    
    def postorder_iteration2(self, root):
        if not root:
            return []
        stack = []
        stack.append(root)
        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            if stack and stack[-1] == node:
                if node.right:
                    stack.append(node.right)
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                    stack.append(node.left)
            else:
                res.append(node.val)
        return res