#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
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

# @lc code=end

print(Solution().isHappy(19))   # True
print(Solution().isHappy(20))   # False
print(Solution().isHappy(2))   # False