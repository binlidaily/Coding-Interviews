#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
import collections
# @lc code=start
# # Time: O(n^2)
# # Space: O(n^2)
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         n = len(s)
#         res = 0
#         for i in range(n):
#             for j in range(i, n):
#                 if self.check(s[i:j+1], k):
#                     res = max(res, j - i + 1)
#         return res
    
#     def check(self, subs, k):
#         hash_map = collections.defaultdict()
#         for ch in subs:
#             hash_map[ch] = hash_map.get(ch, 0) + 1

#         return True if min(hash_map.values()) >= k else False

# Time Limit Exceeded
# 24/28 cases passed (N/A)
# Testcase
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# 1

# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        for ch in set(s):
            if s.count(ch) < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(ch))
        return len(s)

# 28/28 cases passed (28 ms)
# Your runtime beats 88.94 % of python3 submissions
# Your memory usage beats 85.71 % of python3 submissions (13 MB)
# @lc code=end

print(Solution().longestSubstring(s = "aaabb", k = 3))
print(Solution().longestSubstring(s = "ababbc", k = 2))