#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
# Time: O(n)
# Space: O(n)
# class Solution:
#     def reverse(self, x: int) -> int:
#         strx = list(str(x))
#         sign = -1 if strx[0] == '-' else 1
#         if strx[0] == '-':
#             strx = strx[1:]
#         n = len(strx)
#         l, r = 0, n-1
#         while l < r:
#             strx[l], strx[r] = strx[r], strx[l]
#             l += 1
#             r -= 1
#         res = sign * int(''.join(strx))
#         return res if -2147483648 <= res <= 2147483647 else 0
# 1032/1032 cases passed (36 ms)
# Your runtime beats 18.79 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)


# 2. Math
# class Solution:
#     def reverse(self, x: int) -> int:
#         prev, rev = 0, 0
#         while x > 0:
#             rev = rev * 10 + x % 10
#             # overflow
#             print((rev - x % 10) // 10, prev)
#             if (rev - x % 10) // 10 != prev:
#                 return 0
#             prev = rev
#             x = x // 10
#         return rev

# Time: O(n)
# Time: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            # x, mod = divmod(x, 10)
            # rev = rev * 10 + mod
            rev = rev * 10 + x % 10
            x = x // 10
            # overflow
            # if rev > 2147483647 or rev < -2147483648:
            #     return 0
        rev *= sign
        if rev > 2147483647 or rev < -2147483648:
            return 0
        return rev
# 1032/1032 cases passed (28 ms)
# Your runtime beats 78.3 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

# print(Solution().reverse(123))  # 321
print(Solution().reverse(-123))  # -321
# print(Solution().reverse(120))  # 21
# print(Solution().reverse(1534236469))  # 0
# print(Solution().reverse(2147483647))  # 0
# print(Solution().reverse(-2147483648))  # 0