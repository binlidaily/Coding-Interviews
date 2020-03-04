#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        if n <= k:
            return [max(nums)]
        res = []
        # the front of the two-end queue stores the max in the window
        qmax = []
        for i in range(n):
            while qmax and nums[i] > nums[qmax[-1]]:
                qmax.pop()
            qmax.append(i)
            if i >= k - 1:
                while qmax and i - qmax[0] + 1 > k:
                    qmax.pop(0)
                res.append(nums[qmax[0]])
        return res
# 18/18 cases passed (180 ms)
# Your runtime beats 61.53 % of python3 submissions
# Your memory usage beats 80.77 % of python3 submissions (19.6 MB)


# @lc code=end

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(Solution().maxSlidingWindow([1,-1], 1))
print(Solution().maxSlidingWindow([7,2,4], 2))