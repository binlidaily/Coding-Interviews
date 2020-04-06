# -*- coding:utf-8 -*-
# Time: O(n)
# Space: O(n)
class MaxTree:
    def buildMaxTree(self, A, n):
        # write code here
        if not A:
            return []
        res, stack = [], []
        for i in range(n):
            # 根编号为-1
            pos = -1
            # 当前访问的元素比栈顶大 栈中元素需要出栈
            while stack and A[i] > A[stack[-1]]:
                tmp = stack.pop()
                if res[tmp] == -1 or A[i] < A[res[tmp]]:
                    res[tmp] = i
                # 找到了最近的比A[i]大的数
            if stack:
                pos = stack[-1]
            stack.append(i)
            res.append(pos)
        return res
print(MaxTree().buildMaxTree([3,1,4,2], 4))