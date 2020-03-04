#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
import collections
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         hash_map = collections.defaultdict(int)
#         res = 0
#         for num in nums:
#             # drop duplicates
#             if num in hash_map:
#                 continue
#             left = hash_map.get(num - 1, 0)
#             right = hash_map.get(num + 1, 0)
#             cur_max = left + right + 1

#             hash_map[num] = hash_map[num - left] = hash_map[num + right] = cur_max
#             res = max(res, cur_max)
#         return res

# 68/68 cases passed (60 ms)
# Your runtime beats 43.04 % of python3 submissions
# Your memory usage beats 96.3 % of python3 submissions (13.8 MB)


# 2. left
# Time: O(n)
# Space: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                res = max(res, y - x)
        return res

# 68/68 cases passed (56 ms)
# Your runtime beats 66.84 % of python3 submissions
# Your memory usage beats 96.3 % of python3 submissions (13.8 MB)
# @lc code=end

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([]))
print(Solution().longestConsecutive([1,2,0,1]))