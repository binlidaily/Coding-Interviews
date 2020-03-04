#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
# 1. Convert to String
# Time: O(n)
# Space: O(n)
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return self._isPalindrome(str(x))
    
#     def _isPalindrome(self, s):
#         if not s:
#             return True
#         n = len(s)
#         l, r = 0, n - 1
#         while l < r:
#             if s[l] != s[r]:
#                 return False
#             l += 1
#             r -= 1
#         return True

# 11509/11509 cases passed (72 ms)
# Your runtime beats 31.57 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# 2. Same number or not
# Time: O(n)
# Space: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        val = 0
        tmp = x
        while tmp != 0:
            tmp, mod = divmod(tmp, 10)
            val = val * 10 + mod
        return x == val

# 11509/11509 cases passed (64 ms)
# Your runtime beats 52.03 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))