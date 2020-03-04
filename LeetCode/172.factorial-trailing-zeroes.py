#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# from math import factorial
# @lc code=start
# Time: O(n)
# Space: O(1)
# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         # strs = str(factorial(n))
#         prob = 1
#         for i in range(1, n+1):
#             prob *= i
#         strs = str(prob)
#         cnt = 0
#         for ch in strs[::-1]:
#             if ch == '0':
#                 cnt += 1
#             else:
#                 break
#         return cnt

# Time Limit Exceeded
# 500/502 cases passed (N/A)
# Testcase
# 1808548329

# Time: O(logn)
# Space: O(logn)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n < 5 else n // 5 + self.trailingZeroes(n // 5)

# 502/502 cases passed (32 ms)
# Your runtime beats 38.2 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
# @lc code=end

print(Solution().trailingZeroes(3)) # 0
print(Solution().trailingZeroes(5)) # 1
print(Solution().trailingZeroes(7)) # 1