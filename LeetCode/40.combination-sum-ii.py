#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List
# @lc code=start
# Time: O(n^target)
# Space: O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, 0, [], target, res)
        return res
    
    def dfs(self, candidates, start, path, target, res):
        if target == 0:
            res.append(path)
        n = len(candidates)
        for i in range(start, n):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if target >= candidates[i]:
                self.dfs(candidates, i + 1, path + [candidates[i]], target - candidates[i], res)
# 172/172 cases passed (68 ms)
# Your runtime beats 67.83 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().combinationSum2([2,5,2,1,2], 5))