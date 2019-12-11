#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
from typing import List
# @lc code=start
# 1. Brute Force
# Time: O(nm)
# Space: O(n)
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         n1, n2 = len(nums1), len(nums2)
#         res = [-1 for _ in range(n1)]
#         for i in range(n1):
#             j = 0
#             while j < n2:
#                 if nums1[i] == nums2[j]:
#                     break
#                 j += 1
            
#             for k in range(j+1, n2):
#                 if nums2[k] > nums2[j]:
#                     res[i] = nums2[k]
#                     break
#         return res
# 17/17 cases passed (320 ms)
# Your runtime beats 5 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

import collections
# 1.1 Brute Force
# Time: O(nm)
# Space: O(n)
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         n1, n2 = len(nums1), len(nums2)
#         dic = collections.defaultdict()
#         res = [-1 for _ in range(n1)]
#         for i in range(n2):
#             dic[nums2[i]] = i
#         for i in range(n1):
#             j = dic[nums1[i]]
#             for k in range(j+1, n2):
#                 if nums2[k] > nums2[j]:
#                     res[i] = nums2[k]
#                     break
#         return res
# 17/17 cases passed (44 ms)
# Your runtime beats 95.31 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)


# 2. Hash Table + Stack
# Time: O(n)
# Space: O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        if not nums2:
            return [-1] * len(nums1)
        stack = []
        greater = {}
        res = []
        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)
        
        for num in nums1:
            res.append(greater.get(num, -1))
        return res
# 17/17 cases passed (64 ms)
# Your runtime beats 38.05 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
# @lc code=end

print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))