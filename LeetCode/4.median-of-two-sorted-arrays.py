#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List
# @lc code=start
# Time: O(m+n)
# space: O(m+n)
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if not nums1 and nums2:
#             n2 = len(nums2)
#             if n2 % 2 == 1:
#                 return nums2[n2 // 2]
#             else:
#                 return (nums2[n2 // 2 - 1] + nums2[n2 // 2]) / 2
#         elif not nums2 and nums1:
#             n1 = len(nums1)
#             if n1 % 2 == 1:
#                 return nums1[n1 // 2]
#             else:
#                 return (nums1[n1 // 2 - 1] + nums1[n1 // 2]) / 2
#         else:
#             nums = []
#             n1, n2 = len(nums1), len(nums2)
#             i, j = 0, 0
#             while i < n1 and j < n2:
#                 if nums1[i] <= nums2[j]:
#                     nums.append(nums1[i])
#                     i += 1
#                 else:
#                     nums.append(nums2[j])
#                     j += 1
#             if i < n1:
#                 nums += nums1[i:]
#             elif j < n2:
#                 nums += nums2[j:]
#             # print('nums', nums)
#             # print(n1, n2, n1 + n2, len(nums), i, j)
#             if (n1 + n2) % 2 == 1:
#                 return nums[(n1+n2) // 2]
#             else:
#                 return (nums[(n1+n2) // 2 - 1] + nums[(n1+n2) // 2]) / 2
# 2085/2085 cases passed (92 ms)
# Your runtime beats 84.05 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# Time: O(log(m+n))
# space: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        # Make sure n1 <= n2
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1) // 2
        l, r = 0, n1
        while l < r:
            m1 = (l+r) >> 1
            m2 = k - m1
            if nums1[m1] <= nums2[m2-1]:
                l = m1 + 1
            else:
                r = m1
        m1, m2 = l, k - l
        c1 = max(nums1[m1-1] if m1 > 0 else float('-inf'), nums2[m2-1] if m2 > 0 else float('-inf'))
        if (n1 + n2) % 2 == 1:
            return c1
        
        c2 = min(nums1[m1] if m1 < n1 else float('inf'), nums2[m2] if m2 < n2 else float('inf'))
        return (c1 + c2) / 2
# 2085/2085 cases passed (80 ms)
# Your runtime beats 99.41 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().findMedianSortedArrays(nums1 = [1, 3], nums2 = [2]))   # 2.0
print(Solution().findMedianSortedArrays(nums1 = [1, 2], nums2 = [3, 4]))   # 2.5
print(Solution().findMedianSortedArrays([3], [-2,-1]))   # 2.5