#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
import collections
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hash_map = collections.defaultdict(int)
#         for num in nums:
#             if num not in hash_map:
#                 hash_map[num] = 1
#             else:
#                 hash_map[num] += 1
#         vals = sorted(hash_map.values())
#         threshold = vals[-k]
#         res = []
#         for key, val in hash_map.items():
#             if val >= threshold:
#                 res.append(key)
#         return res

# 21/21 cases passed (92 ms)
# Your runtime beats 99.41 % of python3 submissions
# Your memory usage beats 6.25 % of python3 submissions (17.3 MB)

import collections
import heapq
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        frequency = collections.Counter(nums)
        heap = []
        for key, val in frequency.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        res = []
        while k > 0:
            item = heapq.heappop(heap)
            res.append(item[1])
            k -= 1
        return res[::-1]

# 21/21 cases passed (100 ms)
# Your runtime beats 91.02 % of python3 submissions
# Your memory usage beats 6.25 % of python3 submissions (17.1 MB)
# @lc code=end

print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(Solution().topKFrequent(nums = [1], k = 1))