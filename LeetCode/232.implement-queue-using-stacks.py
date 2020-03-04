#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.helper = []

    def pour(self, push_stack, helper):
        if not any(push_stack):
            return
        while push_stack:
            helper.append(push_stack.pop())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not any(self.push_stack) and not self.helper:
            return None

        if not any(self.helper):
            self.pour(self.push_stack, self.helper)

        return self.helper.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not any(self.push_stack) and not self.helper:
            return None
        
        if not any(self.helper):
            self.pour(self.push_stack, self.helper)
        
        return self.helper[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not any(self.push_stack) and not self.helper:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# 17/17 cases passed (20 ms)
# Your runtime beats 98.55 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=end

