#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
from typing import List
# @lc code=start
# Time: O(mnlog(mn))
# Space: O(mn)
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         nums = []
#         for row in matrix:
#             nums += row
#         nums.sort()
#         return nums[k-1]

# 85/85 cases passed (176 ms)
# Your runtime beats 90.28 % of python3 submissions
# Your memory usage beats 9.09 % of python3 submissions (18.6 MB)


# 2. Binary Search
# Time: O(mnlog(mn))
# Space: O(mn)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        if k == n ** 2:
            return matrix[-1][-1]
        if k == 1:
            return matrix[0][0]
        
        low, high = matrix[0][0], matrix[-1][-1]

        while low < high:
            mid = low + (high - low) // 2
            j, cnt = 0, 0
            for i in range(n - 1, -1, -1):
                while j < n and matrix[i][j] <= mid:
                    j += 1
                cnt += j
                if cnt > k:
                    break
            if cnt < k:
                low = mid + 1
            else:
                high = mid
        return low

# 85/85 cases passed (168 ms)
# Your runtime beats 98.03 % of python3 submissions
# Your memory usage beats 9.09 % of python3 submissions (18.7 MB)

# Min Heap
# import heapq
# Time: O(mnlog(mn))
# Space: O(nlogn)
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         if not matrix:
#             return
#         r, c = len(matrix), len(matrix[0])
#         min_heap = [(matrix[0][0], 0, 0)]
#         res = None
#         for _ in range(k):
#             res, i, j = heapq.heappop(min_heap)
#             if j == 0 and i + 1 < r:
#                 heapq.heappush(min_heap, (matrix[i + 1][j], i + 1, j))
#             if j + 1 < c:
#                 heapq.heappush(min_heap, (matrix[i][j + 1], i, j + 1))
#         print(len(min_heap))
#         return res

# 85/85 cases passed (224 ms)
# Your runtime beats 45.98 % of python3 submissions
# Your memory usage beats 9.09 % of python3 submissions (18.6 MB)
# @lc code=end

print(Solution().kthSmallest(matrix = [[ 1,  5,  9],[10, 11, 13],[12, 13, 15]], k = 8))