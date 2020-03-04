#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         n = len(prices)
#         min_v = float('inf')
#         dp = [0 for _ in range(n+1)]
        
#         for i in range(n):
#             dp[i+1] = max(dp[i], prices[i] - min_v)
#             if min_v > prices[i]:
#                 min_v = prices[i]
#         return dp[n]
# 200/200 cases passed (76 ms)
# Your runtime beats 39.56 % of python3 submissions
# Your memory usage beats 55.17 % of python3 submissions (14 MB)

# 2. Directly write
# Time: O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for elem in prices[1:]:
            if elem < min_price:
                min_price = elem
                
            if (elem - min_price) > max_profit:
                max_profit = elem - min_price
                
        return max_profit 
# 200/200 cases passed (56 ms)
# Your runtime beats 97.72 % of python3 submissions
# Your memory usage beats 96.55 % of python3 submissions (13.8 MB)
# @lc code=end

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))