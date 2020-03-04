#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#
from typing import List
# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        sumT = 0
        n = len(timeSeries)
        for i in range(n):
            if i >= 1 and duration > timeSeries[i] - timeSeries[i-1]:
                sumT += timeSeries[i] - timeSeries[i-1]
            else:
                sumT += duration
        return sumT

# 39/39 cases passed (280 ms)
# Your runtime beats 66.52 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.2 MB)

# @lc code=end

print(Solution().findPoisonedDuration([1,4], 2))    # 4
print(Solution().findPoisonedDuration([1,2], 2))    # 3
print(Solution().findPoisonedDuration([1,2,3,4,5], 5))    # 9