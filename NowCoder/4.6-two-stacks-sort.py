# -*- coding:utf-8 -*-
# Time: O(n^2)
# Space: O(n)
class TwoStacks:
    def twoStacksSort(self, numbers):
        # write code here
        if not numbers:
            return []
        helper = []
        while numbers:
            top = numbers.pop()
            
            while any(helper) and top > helper[-1]:
                numbers.append(helper.pop())
            
            helper.append(top)
        return helper

print(TwoStacks().twoStacksSort([5, 4, 3, 2, 1]))