#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
from typing import List
import math
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        min_v, max_v = min(nums), max(nums)
        size = math.ceil((max_v - min_v) / (len(nums) - 1))
        # bucket store min_v and max_v
        bucket = [[None, None] for _ in range((max_v - min_v) // size + 1)]
        for num in nums:
            bckt = bucket[(num - min_v) // size]
            bckt[0] = num if bckt[0] is None else min(bckt[0], num)
            bckt[1] = num if bckt[1] is None else max(bckt[1], num)
        bucket = [bckt for bckt in bucket if bckt[0] is not None]
        
        res = 0
        for i in range(1, len(bucket)):
            res = max(res, bucket[i][0] - bucket[i - 1][1])
        return res
# 18/18 cases passed (68 ms)
# Your runtime beats 53.43 % of python3 submissions
# Your memory usage beats 66.67 % of python3 submissions (13.7 MB)

# @lc code=end

print(Solution().maximumGap([3,6,9,1]))