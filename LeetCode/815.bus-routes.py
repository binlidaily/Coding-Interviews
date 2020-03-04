#
# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#
from typing import List
import collections
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        stop_board = collections.defaultdict()
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stop_board:
                    stop_board[stop] = [bus]
                else:
                    stop_board[stop].append(bus)
        queue = collections.deque([S])
        visited = set()

        res = 0
        while queue:
            res += 1
            size_stops_reach = len(queue)
            for _ in range(size_stops_reach):
                cur_stop = queue.popleft()
                for bus in stop_board[cur_stop]:
                    if bus in visited:
                        continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == T:
                            return res
                        queue.append(stop)
        return -1
# 45/45 cases passed (392 ms)
# Your runtime beats 92 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (31.6 MB)

# @lc code=end

