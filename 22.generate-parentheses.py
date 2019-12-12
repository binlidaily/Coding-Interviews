#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List
# @lc code=start
# Time: O()
# Space: O()
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        left, right = n, n
        res = []
        self.dfs(left, right, '', res)
        return res
    
    def dfs(self, left, right, path, res):
        if left > right :
            return
        if left <= 0 and right <= 0:
            res.append(path)
            return
        
        if left > 0:
            self.dfs(left - 1, right, path + '(', res)
        
        if right > 0:
            self.dfs(left, right - 1, path + ')', res)
# 8/8 cases passed (36 ms)
# Your runtime beats 74.71 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=end

print(Solution().generateParenthesis(3))