#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        key = self.counter(N)
        for i in range(32):
            if self.counter(1 << i) == key:
                return True
        return False
    
    def counter(self, num):
        res = 0
        while num != 0:
            res += pow(10, num % 10)
            num //= 10
        return res
# 135/135 cases passed (32 ms)
# Your runtime beats 56.63 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().reorderedPowerOf2(46))