#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List
# @lc code=start
# Time: O(n^target)
# Space: O(n)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, 0, [], target, res)
        return res
    
    def dfs(self, candidates, start, path, target, res):
        if target == 0:
            res.append(path)

        n = len(candidates)
        for i in range(start, n):
            if target >= candidates[i]:
                self.dfs(candidates, i, path + [candidates[i]], target - candidates[i], res)
# 168/168 cases passed (56 ms)
# Your runtime beats 94.05 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)


# @lc code=end

print(Solution().combinationSum([2,3,6,7], 7))