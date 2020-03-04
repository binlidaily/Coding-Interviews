#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from typing import List
# @lc code=start
# Time: O()
# Space: O()
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k < 0 or k > n:
            return []
        res = []
        self.dfs(n, k, 1, [], res)
        return res
    
    def dfs(self, n, k, start, path, res):
        if start > n+1:
            return
        if path and len(path) == k:
            res.append(path)
        
        for i in range(start, n+1):
            self.dfs(n, k, i+1, path + [i], res)

# 27/27 cases passed (616 ms)
# Your runtime beats 45.02 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.2 MB)

# @lc code=end

print(Solution().combine(4, 2))