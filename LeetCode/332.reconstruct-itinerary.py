#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (33.99%)
# Likes:    1273
# Dislikes: 797
# Total Accepted:    119.5K
# Total Submissions: 351.5K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
# 
# Note:
# 
# 
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# 
# 
# Example 1:
# 
# 
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# 
# 
# Example 2:
# 
# 
# Input:
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.
# 
# 
#
import collections
from typing import List

# @lc code=start
# post visit
# Time: O(nlogn)
# Space: O(n)
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         targets = collections.defaultdict(list)
#         for start, end in sorted(tickets)[::-1]:
#             # end is sorted
#             targets[start].append(end)
#         routes = []

#         def visit(airport):
#             while targets[airport]:
#                 visit(targets[airport].pop())
#             routes.append(airport)

#         visit('JFK')
#         return routes[::-1]

# 80/80 cases passed (76 ms)
# Your runtime beats 87.28 % of python3 submissions
# Your memory usage beats 84.62 % of python3 submissions (13.2 MB)


# Time: O(nlogn)
# Space: O(n)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]

# 80/80 cases passed (80 ms)
# Your runtime beats 70.58 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))

# import unittest
# class Test(unittest.TestCase):
#     inp = [[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]]
#     outp = [["JFK", "MUC", "LHR", "SFO", "SJC"], ["JFK","ATL","JFK","SFO","ATL","SFO"]]

#     def test_unique(self):
#         res = []
#         for x in self.inp:
#             res.append(Solution().findItinerary(x))
#         self.assertEquals(self.outp, res)

# if __name__ == "__main__":
#     unittest.main()