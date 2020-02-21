#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # return a if b == 0 else self.getSum(a ^ b, (a & b) << 1)
        
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        # MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

# 13/13 cases passed (24 ms)
# Your runtime beats 84.85 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().getSum(a = 1, b = 2))
print(Solution().getSum(a = -2, b = 3))