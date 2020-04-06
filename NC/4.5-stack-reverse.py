# -*- coding:utf-8 -*-

class StackReverse:
    def get(self, stack):
        """remove the number on the bottom and return it"""
        top = stack.pop()
        if not stack:
            return top
        else:
            bottom = self.get(stack)
            stack.append(top)
            return bottom

    def reverseStack(self, stack, n):
        if not stack:
            return
        bottom = self.get(stack)
        self.reverseStack(stack, n-1)
        stack.append(bottom)
        return stack

print(StackReverse().reverseStack([1, 2, 3, 4, 5], 5))