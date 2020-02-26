#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
from typing import List
import collections
# @lc code=start
# 1. Brute Force
# Time: O(nm)
# Space: O(n)
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         ns, np = len(s), len(p)
#         res = []
#         for i in range(ns-np+1):
#             if self.is_anagrams(s[i:i+np], p):
#                 res.append(i)
#         return res

#     def is_anagrams(self, s, p):
#         s_dict = collections.defaultdict()
#         p_dict = collections.defaultdict()
#         for ch in s:
#             s_dict[ch] = s_dict.get(ch, 0) + 1

#         for ch in p:
#             p_dict[ch] = p_dict.get(ch, 0) + 1
        
#         return s_dict == p_dict

# Time Limit Exceeded
# 34/36 cases passed (N/A)

# 2. Hash Table
# Time: O(nm)
# Space: O(n)
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         ns, np = len(s), len(p)
#         p_dict = collections.defaultdict()
#         for ch in p:
#             p_dict[ch] = p_dict.get(ch, 0) + 1
#         res = []
#         for i in range(ns-np+1):
#             s_dict = collections.defaultdict()
#             for j in range(i, i+np):
#                 s_dict[s[j]] = s_dict.get(s[j], 0) + 1
#             if s_dict == p_dict:
#                 res.append(i)
#             else:
#                 s_dict[s[i]] = s_dict[s[i]] - 1
#                 if s_dict[s[i]] == 0:
#                     s_dict.pop(s[i])
#         return res

# Time Limit Exceeded
# 34/36 cases passed (N/A)

# Time: O(n)
# Space: O(1)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if np > ns:
            return []
        shash, phash = [0] * 123, [0] * 123
        res = []
        for ch in p:
            phash[ord(ch)] += 1
        for i in range(np-1):
            shash[ord(s[i])] += 1
        for i in range(np-1, ns):
            shash[ord(s[i])] += 1
            if i - np >= 0:
                shash[ord(s[i - np])] -= 1
            if shash == phash:
                res.append(i - np + 1)
        return res

# 36/36 cases passed (112 ms)
# Your runtime beats 75.49 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.7 MB)

# @lc code=end

print(Solution().findAnagrams("cbaebabacd", "abc")) # [0, 6]
print(Solution().findAnagrams("abab", "ab"))    # [0, 1, 2]