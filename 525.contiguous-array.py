#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_sum = 0
        max_length = 0
        table = {0 : 0}
        for i, num in enumerate(nums, 1):
            if num == 0:
                cur_sum += -1
            else:
                cur_sum += 1
            if cur_sum in table:
                max_length = max(max_length, i - table[cur_sum])
            else:
                table[cur_sum] = i
        return max_length
# 555/555 cases passed (956 ms)
# Your runtime beats 28.19 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (17.1 MB)
# @lc code=end

print(Solution().findMaxLength([0,1,1]))  # 2