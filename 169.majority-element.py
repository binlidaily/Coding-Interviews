#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]

# 44/44 cases passed (172 ms)
# Your runtime beats 85.91 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14 MB)

# Time: O(n)
# Space: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = 0
        for i in range(32):
            mask = 1 << i
            count = 0
            for num in nums:
                if num & mask:
                    count += 1
            if count > n // 2:
                majority |= mask
        return majority if majority >> 31 == 0 else majority - (1 << 32)

# 44/44 cases passed (172 ms)
# Your runtime beats 85.91 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14 MB)


# @lc code=end

print(Solution().majorityElement([3,2,3]))  # 3
print(Solution().majorityElement([2,2,1,1,1,2,2]))  # 2