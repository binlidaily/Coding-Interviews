from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        res = []
        for pos, i in enumerate(index):
            res.insert(i, nums[pos])
        return res

print(Solution().createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]), [0,4,1,3,2])