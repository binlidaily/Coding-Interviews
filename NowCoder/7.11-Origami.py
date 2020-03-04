# -*- coding:utf-8 -*-
# Time: O(n)
# Space: O(1)
class FoldPaper:
    def foldPaper(self, n):
        res = []
        self.inorder(0, n, True, res)
        return res
        
    def inorder(self, i, n, is_down, res):
        if i >= n:
            return
        self.inorder(i + 1, n, True, res)
        res.append('down' if is_down else 'up')
        self.inorder(i + 1, n, False, res)