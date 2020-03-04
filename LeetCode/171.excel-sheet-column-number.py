#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
# Time: O(n)
# Space: O(n)
# class Solution:
#     def titleToNumber(self, s: str) -> int:
#         keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         values = range(1, 27)
#         hash_map = dict(zip(keys, values))
#         res = 0
#         for ch in s:
#             res = res * 26 + hash_map[ch]
#         return res

# 1000/1000 cases passed (32 ms)
# Your runtime beats 53.41 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)

from functools import reduce
# Time: O(n)
# Space: O(n)
class Solution:
    def titleToNumber(self, s: str) -> int:
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])

# 1000/1000 cases passed (32 ms)
# Your runtime beats 53.41 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().titleToNumber('A'))
print(Solution().titleToNumber('AB'))
print(Solution().titleToNumber('ZY'))