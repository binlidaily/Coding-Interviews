#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) <= 1:
            return 0
        n = len(prices)
        buy = [0 for _ in range(n)]
        sell = [0 for _ in range(n)]
        buy[0] = -prices[0] - fee
        for i in range(1, n):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i] - fee) # keep the same as day i-1, or buy from sell status at day i-1
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])  # keep the same as day i-1, or sell from buy status at day i-1
        return sell[n - 1]
# 44/44 cases passed (920 ms)
# Your runtime beats 17.06 % of python3 submissions
# Your memory usage beats 12.5 % of python3 submissions (19.3 MB)

# @lc code=end

print(Solution().maxProfit([1,3,2,8,4,9], 2))