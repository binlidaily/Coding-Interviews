#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
# Time: O(1)
# Space: O(1)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         oribin = '{0:032b}'.format(n)
#         cnt = 0
#         for ch in oribin:
#             if ch == '1':
#                 cnt += 1
#         return cnt

# 601/601 cases passed (28 ms)
# Your runtime beats 73.21 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# Time: O(1)
# Space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            if n & 1:
                res += 1
            n >>= 1
        return res

# 601/601 cases passed (24 ms)
# Your runtime beats 91.96 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# @lc code=end

