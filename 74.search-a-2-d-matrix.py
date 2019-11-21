#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import List
# @lc code=start
# Time: O(nlogm)
# Space: O(n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0:
            return False
        h, w = len(matrix), len(matrix[0])
        r = -1
        for i in range(h):
            if w-1 >= 0 and matrix[i][w-1] >= target:
                r = i
                break

        if r == -1:
            return False
        if self.binary_search(matrix[r], target) == -1:
            return False
        else:
            return True
    
    def binary_search(self, nums, target):
        if not nums:
            return -1
        
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
# 136/136 cases passed (68 ms)
# Your runtime beats 92.86 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions (14.9 MB)


# @lc code=end

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
print(Solution().searchMatrix([[]], 1))
print(Solution().searchMatrix([[1]], 1))