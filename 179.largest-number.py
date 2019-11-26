#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
from typing import List
# @lc code=start
class compare(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # res = ''.join(sorted(map(str, nums), key=lambda x, y: int(x+y)-int(y+x)))
        res = ''.join(sorted([str(v) for v in nums], key=compare))
        return res if res[0]!='0' else '0'
# 222/222 cases passed (36 ms)
# Your runtime beats 93.4 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().largestNumber([10, 2]))