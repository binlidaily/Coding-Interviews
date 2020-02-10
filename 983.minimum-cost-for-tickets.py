#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#
from typing import List

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = set(days)
        dp = [0 for i in range(days[-1] + 1)]
        for day_i in range(1, days[-1] + 1):
            if day_i not in travel_days:
                dp[day_i] = dp[day_i - 1]
                continue
            dp[day_i] = min(dp[max(0, day_i - 1)] + costs[0],
                        dp[max(0, day_i - 7)] + costs[1],
                        dp[max(0, day_i - 30)] + costs[2])
        return dp[-1]

# 66/66 cases passed (36 ms)
# Your runtime beats 89.82 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))   # 11
print(Solution().mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))   # 17