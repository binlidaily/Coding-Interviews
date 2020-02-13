#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         n = len(gas)
#         for i in range(n):
#             tank = 0
#             flag = True
#             for j in range(n):
#                 idx = (i + j) % n
#                 tank += gas[idx]
#                 if tank < cost[idx]:
#                     flag = False
#                     break
#                 tank -= cost[idx]
#             if flag:
#                 return i
#         return -1

# 31/31 cases passed (3788 ms)
# Your runtime beats 5.1 % of python3 submissions
# Your memory usage beats 93.75 % of python3 submissions (13.8 MB)

# 2. O(n)
# Time: O(n)
# Space: O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas, sum_cost, start, tank = 0, 0, 0, 0
        for i in range(len(gas)):
            sum_gas += gas[i]
            sum_cost += cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start = i + 1
            
        return start if sum_gas >= sum_cost else -1

# 31/31 cases passed (48 ms)
# Your runtime beats 90.54 % of python3 submissions
# Your memory usage beats 93.75 % of python3 submissions (13.8 MB)
# @lc code=end

print(Solution().canCompleteCircuit(gas  = [1,2,3,4,5], cost = [3,4,5,1,2]))
print(Solution().canCompleteCircuit(gas  = [2,3,4], cost = [3,4,3]))