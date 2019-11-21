#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
from typing import List
# @lc code=start
# Time: O(n^size)
# Sapce: O(n)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(k, 1, n, [], res)
        return res

    def dfs(self, size, start, target, path, res):
        if target == 0 and len(path) == size:
            res.append(path)
        
        l = len(path)
        for i in range(start, 10):
            if target >= i and l <= size:
                self.dfs(size, i + 1, target - i, path + [i], res)
# 18/18 cases passed (28 ms)
# Your runtime beats 96.4 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().combinationSum3(3, 9))