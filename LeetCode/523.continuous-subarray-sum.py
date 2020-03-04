#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k == 0 :
            for i in range(1, n):
                if nums[i] == nums[i - 1] and nums[i] == 0:
                    return True
            return False
        k = abs(k)
        if n >= 2 * k:
            return True
        sum = [0]
        for num in nums:
            sum.append((sum[-1] + num) % k)
        
        dic = {}
        for i in range(len(sum)):
            if sum[i] in dic:
                if i - dic[sum[i]] >= 2:
                    return True
            else:
                dic[sum[i]] = i
        return False
# Runtime: 220 ms, faster than 93.30%
# Memory Usage: 13.3 MB, less than 71.43%

# @lc code=end

