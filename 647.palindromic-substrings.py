#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
# 1. Brute Force
# Time: O(n^2)
# Space: O(1)
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         res = []
#         for i in range(n):
#             for j in range(i, n):
#                 if self.is_palindromic(s[i:j+1]):
#                     res.append(s[i:j+1])
#         return len(res)

#     def is_palindromic(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
#         while l <= r:
#             if s[l] != s[r]:
#                 return False
#             l += 1
#             r -= 1
#         return True
# Time Limit Exceeded
# 128/130 cases passed (N/A)


# Time: O(n^2)
# Space: O(1)
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         res = 0
#         for i in range(n):
#             res += self.count(s, i, i) + self.count(s, i, i+1)
#         return res

#     def count(self, s: str, i: int, j:int) -> bool:
#         n = len(s)
#         cnt = 0
#         while i >= 0 and j < n:
#             if s[i] == s[j]:
#                 cnt += 1
#             else:
#                 break
#             i -= 1
#             j += 1
#         return cnt

# 130/130 cases passed (116 ms)
# Your runtime beats 86.22 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)

# 3. DP
# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # j - i < 3: AXA
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i+1][j-1])
                if dp[i][j]:
                    cnt += 1
        return cnt

# 130/130 cases passed (352 ms)
# Your runtime beats 29.95 % of python3 submissions
# Your memory usage beats 34.61 % of python3 submissions (21.4 MB)
# @lc code=end

print(Solution().countSubstrings("abc"))
print(Solution().countSubstrings("aaa"))
print(Solution().countSubstrings("fdsklf")) # 6