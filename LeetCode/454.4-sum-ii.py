#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        ab_hash = {}
        for a in A:
            for b in B:
                ab_hash[a + b] = ab_hash.get(a + b, 0) + 1
        for c in C:
            for d in D:
                if -c - d in ab_hash:
                    res += ab_hash[-c - d]
        return res
# 48/48 cases passed (636 ms)
# Your runtime beats 5.05 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (33.6 MB)
# @lc code=end

print(Solution().fourSumCount(A = [ 1, 2], B = [-2,-1], C = [-1, 2], D = [ 0, 2]))