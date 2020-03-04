#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
# Time: O(nlogn)
# Space: O(nlogn)
# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix or not matrix[0]:
#             return False
        
#         r = len(matrix)
#         for i in range(r):
#             if matrix[i][-1] < target:
#                 continue
#             if self.binary_search(matrix[i], target):
#                 return True
#         return False
    
#     def binary_search(self, nums, target):
#         if not nums:
#             return False
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = l + (r - l) // 2
#             if nums[mid] == target:
#                 return True
#             elif nums[mid] > target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return False

# 129/129 cases passed (32 ms)
# Your runtime beats 82.94 % of python3 submissions
# Your memory usage beats 88.89 % of python3 submissions (17.4 MB)


# Time: O(m+n)
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False

# 129/129 cases passed (40 ms)
# Your runtime beats 36.96 % of python3 submissions
# Your memory usage beats 92.59 % of python3 submissions (17.4 MB)
# @lc code=end

print(Solution().searchMatrix([[1,   4,  7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]], 5))   # True
print(Solution().searchMatrix([[1,   4,  7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]], 20))   # False