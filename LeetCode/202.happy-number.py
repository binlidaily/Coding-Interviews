#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution1:
    def isHappy(self, n: int) -> bool:
        visited = set()
        visited.add(n)
        while n != 1:
            strs = str(n)
            ssum = 0
            for num in strs:
                ssum += int(num) ** 2
            if ssum in visited:
                return False
            else:
                visited.add(ssum)
            n = ssum
        return True

# 401/401 cases passed (36 ms)
# Your runtime beats 34.19 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# Wrong Answer!
class Solution:
    def isHappy(self, n: int) -> bool:
        return self._isHappy(n, None)
    
    def _isHappy(self, n: int, pre: int) -> bool:
        if n == 1:
            return True
        if pre and pre == n:
            return False
        pre = n
        stack = []
        while n != 0:
            stack.append(n % 10)
            n = n // 10
            # print('n', n)
        new = 0
        print('*'*10)
        while stack:
            top = stack.pop()
            new = new * 10 + top ** 2
        print(new, pre)
        return self._isHappy(new, pre)

# @lc code=end

print(Solution().isHappy(19))   # True
# print(Solution().isHappy(20))   # False
# print(Solution().isHappy(2))   # False