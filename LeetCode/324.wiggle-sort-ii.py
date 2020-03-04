#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#
from typing import List
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
# class Solution:
#     def wiggleSort(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         nums.sort()
#         mid = len(nums[::2])
#         nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]

# 44/44 cases passed (172 ms)
# Your runtime beats 86.52 % of python3 submissions
# Your memory usage beats 11.11 % of python3 submissions (15.7 MB)

# from random import randint
# Time: O(n)
# Space: O(1)
# class Solution:
#     def wiggleSort(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         def findKthLargest(nums, k):
#             left, right = 0, len(nums) - 1
#             while left <= right:
#                 pivot_idx = randint(left, right)
#                 new_pivot_idx = partitionAroundPivot(left, right, pivot_idx, nums)
#                 if new_pivot_idx == k - 1:
#                     return nums[new_pivot_idx]
#                 elif new_pivot_idx > k - 1:
#                     right = new_pivot_idx - 1
#                 else:  # new_pivot_idx < k - 1.
#                     left = new_pivot_idx + 1

#         def partitionAroundPivot(left, right, pivot_idx, nums):
#             pivot_value = nums[pivot_idx]
#             new_pivot_idx = left
#             nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
#             for i in range(left, right):
#                 if nums[i] > pivot_value:
#                     nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
#                     new_pivot_idx += 1
#             nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
#             return new_pivot_idx

#         def reversedTriPartitionWithVI(nums, val):
#             def idx(i, N):
#                 return (1 + 2 * (i)) % N

#             N = len(nums) // 2 * 2 + 1
#             i, j, n = 0, 0, len(nums) - 1
#             while j <= n:
#                 if nums[idx(j, N)] > val:
#                     nums[idx(i, N)], nums[idx(j, N)] = nums[idx(j, N)], nums[idx(i, N)]
#                     i += 1
#                     j += 1
#                 elif nums[idx(j, N)] < val:
#                     nums[idx(j, N)], nums[idx(n, N)] = nums[idx(n, N)], nums[idx(j, N)]
#                     n -= 1
#                 else:
#                     j += 1

#         mid = (len(nums) - 1) // 2
#         findKthLargest(nums, mid + 1)
#         reversedTriPartitionWithVI(nums, nums[mid])

# 44/44 cases passed (3140 ms)
# Your runtime beats 5.02 % of python3 submissions
# Your memory usage beats 11.11 % of python3 submissions (15.4 MB)


# import statistics
# class Solution:
#     def wiggleSort(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         mid = statistics.median(nums)
#         n = len(nums)
        
#         # three-parition
#         i, j, k = 0, 0, n
#         while j < k:
#             if nums[j] > mid:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#                 j += 1
#             elif nums[j] < mid:
#                 k -= 1
#                 nums[k], nums[j] = nums[j], nums[k]
#             else:
#                 j += 1

#         # wigglely rearrage 
#         h = n//2    # bug: len h needs to the <= real half
#         nums[::2], nums[1::2] = nums[h:], nums[:h]
#         print(nums)
# update: if do 3-partition inversely (L-M-S), the wigglely rearrange part is simpler
#           but be careful the len of right and left changes
        
"""
Method Logic:
    1. find median of the list in O(n) time and O(1) space -> leetcode 215
    2. three-parititon algorithm to rearrange the array to SMALL->MEDIAN->LARGE TC=O(n) SC=O(1)
        https://en.wikipedia.org/wiki/Dutch_national_flag_problem#Pseudocode
    3. rearrange the array to ODD-IDX = SMALL; EVEN-IDX = LARGE; with MEDIAN at two edge (same with previous submission) 
        TC = O(n); SC = O(n) because list slicing idx copys array

"""


import statistics

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        med= statistics.median(nums)
        l, m, r=0, 0, len(nums) - 1
        
        while m<=r:
            m_ind=self.A(m,nums)
            if nums[m_ind]>med:
                l_ind=self.A(l,nums)
                nums[l_ind],nums[m_ind]=nums[m_ind],nums[l_ind]                               
                l+=1
                m+=1
            elif nums[m_ind]<med: 
                r_ind=self.A(r,nums)
                nums[m_ind],nums[r_ind]=nums[r_ind],nums[m_ind]
                r-=1
            else:
                m+=1
        

    def A(self,i,nums):  
        n=len(nums)
        return(1+2*(i)) % (n|1)
# 44/44 cases passed (228 ms)
# Your runtime beats 25.71 % of python3 submissions
# Your memory usage beats 11.11 % of python3 submissions (15.9 MB)
# @lc code=end

print(Solution().wiggleSort([1, 5, 1, 1, 6, 4]))    # 