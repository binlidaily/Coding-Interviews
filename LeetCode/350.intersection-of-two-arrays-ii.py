#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
from typing import List
import collections
# @lc code=start
# Time: O(n+m)
# Space: O(n)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = collections.Counter(nums1)
        res = []
        for num in nums2:
            if num in hash_map and hash_map[num] > 0:
                res.append(num)
                hash_map[num] -= 1
        return res
        
# 61/61 cases passed (48 ms)
# Your runtime beats 56.08 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().intersect(nums1 = [1,2,2,1], nums2 = [2,2]))   # [2, 2]
print(Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))   # [4, 9]