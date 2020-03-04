#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
from typing import List
import heapq
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Sort by the first number in the tuple
        # events = sorted([(L, -H, R) for L, R, H in buildings] + \
        #     list({(R, 0, None) for _, R, _ in buildings}))

        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()
        print(events)
        
        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos: 
                heapq.heappop(live)
            if negH: 
                heapq.heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [ [pos, -live[0][0]] ]
        return res[1:]

# 36/36 cases passed (116 ms)
# Your runtime beats 84.49 % of python3 submissions
# Your memory usage beats 40 % of python3 submissions (17.7 MB)
# @lc code=end

print(Solution().getSkyline([[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]))