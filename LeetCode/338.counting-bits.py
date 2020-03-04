#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
from typing import List
# @lc code=start
# 1. Brute Force
# Time: O(num)
# Space: O(num)
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         res = []
#         for i in range(num+1):
#             cnt = 0
#             while i != 0:
#                 div, mod = divmod(i, 2)
#                 if mod == 1:
#                     cnt += 1
#                 i = div
#             res.append(cnt)
#         return res

# 15/15 cases passed (300 ms)
# Your runtime beats 5.01 % of python3 submissions
# Your memory usage beats 5 % of python3 submissions (19.5 MB)

# Time: O(num)
# Space: O(num)
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(num + 1):
            res[i] = res[i >> 1] + i % 2
        return res
# 15/15 cases passed (88 ms)
# Your runtime beats 56.5 % of python3 submissions
# Your memory usage beats 5 % of python3 submissions (19.6 MB)
# @lc code=end

print(Solution().countBits(2))  # [0,1,1]
print(Solution().countBits(5))  # [0,1,1,2,1,2]