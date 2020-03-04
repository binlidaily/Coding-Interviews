#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        total = 0
        for i in range(n-1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total
# 201/201 cases passed (56 ms)
# Your runtime beats 96.94 % of python3 submissions
# Your memory usage beats 63.42 % of python3 submissions (13.9 MB)
# @lc code=end
