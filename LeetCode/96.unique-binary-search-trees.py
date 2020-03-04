#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0
        G = [0 for _ in range(n+1)]
        G[0], G[1] = 1, 1
        # G(n) = F(1, n) + F(2, n) + ... + F(n, n). 
        # F(i, n) = G(i-1) * G(n-i)	1 <= i <= n 
        for i in range(2, n+1):
            for j in range(i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]
# 19/19 cases passed (28 ms)
# Your runtime beats 79.88 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=end

