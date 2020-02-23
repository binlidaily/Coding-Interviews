#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) <= 1:
#             return 0
#         n = len(prices)
#         rest = [0] * n
#         hold = [-prices[0]] * n
#         sold = [0] * n
#         for i in range(1, n):
#             rest[i] = max(rest[i-1], sold[i-1])
#             hold[i] = max(hold[i-1], rest[i-1] - prices[i])
#             sold[i] = hold[i-1] + prices[i]
#         return max(rest[-1], sold[-1])

# 211/211 cases passed (40 ms)
# Your runtime beats 53.66 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# Time: O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        n = len(prices)
        rest = 0
        hold = -prices[0]
        sold = 0
        for i in range(1, n):
            pre_rest = rest
            rest = max(rest, sold)
            sold = hold + prices[i]
            hold = max(hold, pre_rest - prices[i])
        return max(rest, sold)

# 211/211 cases passed (36 ms)
# Your runtime beats 79.61 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().maxProfit([1,2,3,0,2]))