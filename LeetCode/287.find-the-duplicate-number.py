#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
from typing import List
# @lc code=start
# Time: O(nlogn)
# Space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
        return l

# 53/53 cases passed (76 ms)
# Your runtime beats 28.57 % of python3 submissions
# Your memory usage beats 17.86 % of python3 submissions (15.2 MB)
# @lc code=end

print(Solution().findDuplicate([1,3,4,2,2]))
print(Solution().findDuplicate([3,1,3,4,2]))