#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res

# 8/8 cases passed (32 ms)
# Your runtime beats 98.93 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.8 MB)
# @lc code=end

print(Solution().fizzBuzz(15))