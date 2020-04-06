from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums = sorted(nums, reverse=True)
        n = len(nums)
        for i in range(n):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
        return nums

print(Solution().minSubsequence([4,3,10,9,8]), [10,9])
print(Solution().minSubsequence([4,4,7,6,7]), [7,7,6])
print(Solution().minSubsequence([6]), [6])