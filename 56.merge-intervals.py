#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key = lambda x: x[0])
        for item in intervals:
            if res and item[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], item[1])
            else:
                res.append(item)
        return res
# 169/169 cases passed (104 ms)
# Your runtime beats 18.37 % of python3 submissions
# Your memory usage beats 6.52 % of python3 submissions (14.8 MB)
# @lc code=end

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))