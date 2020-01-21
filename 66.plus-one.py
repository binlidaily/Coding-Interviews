#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]: 
#         res =  int(''.join([str(d) for d in digits])) + 1
#         res = str(res)
#         return [int(num) for num in res]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + [0] * n
# 109/109 cases passed (32 ms)
# Your runtime beats 45.9 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([8,9,9,9]))
print(Solution().plusOne([9, 9]))