#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
# Time: O(n)
# Sapce: O(n)
# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.nums = []

#     def addNum(self, num: int) -> None:
#         if not self.nums:
#             self.nums.append(num)
#         else:
#             n = len(self.nums)
#             for i in range(n):
#                 if self.nums[i] > num:
#                     self.nums = self.nums[:i] + [num] + self.nums[i:]
#                     return
#             self.nums.append(num)

#     def findMedian(self) -> float:
#         n = len(self.nums)
#         if n % 2 == 0:
#             two_sum = self.nums[n // 2 - 1] + self.nums[n // 2]
#             return (two_sum) / 2 if two_sum > 0 else -1 * (abs(two_sum) / 2)
#         else:
#             return self.nums[n // 2] 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Time Limit Exceeded
# 17/18 cases passed (N/A)

import heapq
# Time: O(nlogn)
# Sapce: O(n)
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # the smaller half of the list, use max heap (invert min-heap)
        self.large = [] # the larger half of the list, use min heap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# 18/18 cases passed (192 ms)
# Your runtime beats 82.78 % of python3 submissions
# Your memory usage beats 46.67 % of python3 submissions (23.5 MB)

# @lc code=end

m = MedianFinder()
m.addNum(1)
m.addNum(2)
print(m.findMedian())
m.addNum(3)
print(m.findMedian())

m = MedianFinder()
m.addNum(-1)
print(m.findMedian())
m.addNum(-2)
print(m.findMedian())
m.addNum(-3)
print(m.findMedian())
m.addNum(-4)
print(m.findMedian())
m.addNum(-5)
print(m.findMedian())