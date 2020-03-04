#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
import heapq
from typing import List
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)

# 32/32 cases passed (68 ms)
# Your runtime beats 59.02 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.3 MB)
# @lc code=end

print(Solution().findKthLargest([3,2,1,5,6,4], 2))  # 5
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # 4