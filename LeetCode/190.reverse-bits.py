#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
# Time: O(n)
# Space: O(1)
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         oribin='{0:032b}'.format(n)
#         reversebin=oribin[::-1]
#         return int(reversebin,2)

# 600/600 cases passed (24 ms)
# Your runtime beats 92.77 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# Time: O(1)
# Space: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # res = res * 2 + n % 2
            # n //= 2

            # res = (res << 1) + (n & 1)
            # n >>= 1

            res = res << 1 | (n & 1)
            n >>= 1
        return res

# 600/600 cases passed (32 ms)
# Your runtime beats 50.82 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# 600/600 cases passed (28 ms)
# Your runtime beats 77.33 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# 600/600 cases passed (32 ms)
# Your runtime beats 50.82 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().reverseBits(964176192))