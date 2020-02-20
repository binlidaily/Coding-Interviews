#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
from typing import List
# @lc code=start
# Time: O(n+m)
# Space: O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        for num in nums1:
            if num not in set1:
                set1.add(num)
        res = set()
        for num in nums2:
            if num in set1 and num not in res:
                res.add(num)
        return list(res)

# 60/60 cases passed (40 ms)
# Your runtime beats 90.67 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(Solution().intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))