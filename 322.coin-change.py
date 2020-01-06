#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import List
# @lc code=start
# 1. Brute Force
# Time: O(S^n)
# Space: O(n)
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if not coins or amount < 0:
#             return 0
#         return self.brute_force(coins, 0, amount)
    
#     def brute_force(self, coins, idx, amount):
#         if amount == 0:
#             return 0

#         if idx < len(coins) and amount > 0:
#             max_try = amount // coins[idx]
#             min_coins = float('inf')
#             for i in range(max_try+1):
#                 if i * coins[idx] <= amount:
#                     res = self.brute_force(coins, idx + 1, amount - i * coins[idx])
#                     if res != -1:
#                         min_coins = min(min_coins, res + i)
#             return min_coins if min_coins != float('inf') else -1
#         return -1
# Time Limit Exceeded
# 32/182 cases passed (N/A)

# 2. Memo
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if not coins or amount < 0:
#             return 0
#         memo = [float('inf') for _ in range(amount + 1)]
#         memo[0] = 0
#         return self.brute_force(coins, memo, 0, amount)
    
#     def brute_force(self, coins, memo, idx, amount):
#         if amount == 0:
#             return 0
#         if memo[amount] != float('inf'):
#             return memo[amount]
#         if idx < len(coins) and amount > 0:
#             max_try = amount // coins[idx]
#             # min_coins = float('inf')
#             for i in range(max_try + 1):
#                 if i * coins[idx] <= amount:
#                     res = self.brute_force(coins, memo, idx + 1, amount - i * coins[idx])
#                     if res != -1:
#                         memo[amount] = min(memo[amount], res + i)
#             return memo[amount] if memo[amount] != float('inf') else -1
#         return -1
# Time Limit Exceeded
# 32/182 cases passed (N/A)

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if not coins or amount < 0:
#             return 0
#         memo = [float('inf') for _ in range(amount + 1)]
#         memo[0] = 0
#         return self.brute_force(coins, memo, amount)
    
#     def brute_force(self, coins, memo, amount):
#         if amount < 0:
#             return -1
#         if memo[amount] != float('inf'):
#             return memo[amount]
#         n = len(coins)
#         for i in range(n):
#             res = self.brute_force(coins, memo, amount - coins[i])
#             if res >= 0:
#                 memo[amount] = min(memo[amount], res + 1)
#         return memo[amount] if memo[amount] != float('inf') else -1

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if not coins or amount < 0:
#             return 0
#         memo = [0 for _ in range(amount + 1)]
#         return self.brute_force(coins, memo, amount)
    
#     def brute_force(self, coins, memo, amount):
#         if amount < 0:
#             return -1
#         if amount == 0:
#             return 0
#         if memo[amount] != 0:
#             return memo[amount]
#         min_coins = float('inf')
#         for coin in coins:
#             res = self.brute_force(coins, memo, amount - coin)
#             if res >= 0:
#                 min_coins = min(min_coins, res + 1)
#         memo[amount] = min_coins if min_coins != float('inf') else -1
#         return memo[amount]
# 182/182 cases passed (2100 ms)
# Your runtime beats 8.85 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (15.2 MB)


# 3. DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return 0
        memo = [float('inf') for _ in range(amount + 1)]
        memo[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                memo[i] = min(memo[i], memo[i-coin] + 1)
        return memo[amount] if memo[amount] != float('inf') else -1
# 182/182 cases passed (1368 ms)
# Your runtime beats 57.1 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13 MB)

# @lc code=end

print(Solution().coinChange([1, 2, 5], 11)) # 3
print(Solution().coinChange([431,62,88,428], 9084)) # 26