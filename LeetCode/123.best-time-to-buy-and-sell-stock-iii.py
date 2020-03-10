#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        g = [[0] * 3 for _ in range(n)]
        l = [[0] * 3 for _ in range(n)]
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            for j in range(1, 3):
                l[i][j] = max(g[i - 1][j - 1] + max(diff, 0), l[i - 1][j] + diff)
                g[i][j] = max(l[i][j], g[i - 1][j])
        return g[-1][-1]
# 200/200 cases passed (108 ms)
# Your runtime beats 17.09 % of python3 submissions
# Your memory usage beats 36.36 % of python3 submissions (18.4 MB)

# Time: O(n)
# Space: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        first_trade = []
        n = len(prices)
        lowest = float('inf')
        profit = 0
        for i in range(n):
            lowest = min(prices[i], lowest)
            profit = max(profit, prices[i] - lowest)
            first_trade.append(profit)
        
        total_max = 0
        highest = float('-inf')
        profit = 0
        for i in range(n-1, -1, -1):
            highest = max(highest, prices[i])
            profit = max(profit, highest-prices[i])
            total_max = max(total_max, first_trade[i] + profit)
        return total_max

# 200/200 cases passed (84 ms)
# Your runtime beats 51.62 % of python3 submissions
# Your memory usage beats 72.73 % of python3 submissions (14 MB)
# @lc code=end

print(Solution().maxProfit([3,3,5,0,0,3,1,4]), 6)
print(Solution().maxProfit([1,2,3,4,5]), 4)
print(Solution().maxProfit([7,6,4,3,1]), 0)