#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
import collections
# @lc code=start
# Time: O(n)
# Space: O(n)
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         hash_map = collections.defaultdict()
#         for i, ch in enumerate(s):
#             if ch in hash_map:
#                 hash_map[ch] = (hash_map[ch][0] + 1, hash_map[ch][1], ch)
#             else:
#                 hash_map[ch] = (1, i, ch)

#         values = hash_map.values()
#         res = float('inf')
#         for cnt, idx, ch in values:
#             if cnt == 1 and idx < res:
#                 res = idx
#         return res if res < float('inf') else -1

# 104/104 cases passed (184 ms)
# Your runtime beats 16.71 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# Time: O(n)
# Space: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = collections.defaultdict()
        filter = set()
        for i, ch in enumerate(s):
            if ch not in filter:
                filter.add(ch)
                hash_map[ch] = i
            elif ch in hash_map:
                del hash_map[ch]
        return min(hash_map.values()) if hash_map else -1

# 104/104 cases passed (96 ms)
# Your runtime beats 75.89 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))