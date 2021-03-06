#
# @lc app=leetcode id=1184 lang=python3
#
# [1184] Distance Between Bus Stops
#
# https://leetcode.com/problems/distance-between-bus-stops/description/
#
# algorithms
# Easy (55.28%)
# Likes:    135
# Dislikes: 18
# Total Accepted:    16.6K
# Total Submissions: 30.1K
# Testcase Example:  '[1,2,3,4]\n0\n1'
#
# A bus has n stops numbered from 0 to n - 1 that form a circle. We know the
# distance between all pairs of neighboring stops where distance[i] is the
# distance between the stops number i and (i + 1) % n.
# 
# The bus goes along both directions i.e. clockwise and counterclockwise.
# 
# Return the shortest distance between the given start and destination
# stops.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: distance = [1,2,3,4], start = 0, destination = 1
# Output: 1
# Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: distance = [1,2,3,4], start = 0, destination = 2
# Output: 3
# Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.
# 
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: distance = [1,2,3,4], start = 0, destination = 3
# Output: 4
# Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# distance.length == n
# 0 <= start, destination < n
# 0 <= distance[i] <= 10^4
# 
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution1:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        i = start
        path1, path2 = 0, 0
        n = len(distance)
        while i % n != destination:
            path1 += distance[i % n]
            i += 1
        i = start
        while i != destination:
            i -= 1
            if i < 0:
                i = n - 1
            path2 += distance[i]
        return min(path1, path2)

# 37/37 cases passed (40 ms)
# Your runtime beats 91.41 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.7 MB)


# Time: O(n)
# Space: O(1)
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        
        total_sum = 0
        dist = 0
        n = len(distance)
        for i in range(n):
            if start <= i < destination:
                dist += distance[i]
            total_sum += distance[i]
        return min(dist, total_sum - dist)

# 37/37 cases passed (44 ms)
# Your runtime beats 75 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.7 MB)
# @lc code=end

print(Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1), 1)
print(Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2), 3)
print(Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3), 4)