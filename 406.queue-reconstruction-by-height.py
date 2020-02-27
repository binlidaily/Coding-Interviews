#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))

        res = []
        for p in people:
            res.insert(p[1], p)
        return res

# 37/37 cases passed (96 ms)
# Your runtime beats 84.54 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13 MB)
# @lc code=end

print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))