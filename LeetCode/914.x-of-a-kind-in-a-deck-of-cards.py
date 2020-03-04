#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#
from typing import List
import collections

# @lc code=start
# Time: O(n^2)
# Space: O(n)
# class Solution:
#     def hasGroupsSizeX(self, deck: List[int]) -> bool:
#         n = len(deck)
#         deck.sort()
#         for i in range(2, n+1):
#             if n % i == 0:
#                 # count = n // i
#                 flag = True
#                 j = 0
#                 while j < n:
#                     if len(set(deck[j:j+i])) != 1:
#                         flag = False
#                     j += i
#                 if flag:
#                     return True
#         return False
# 69/69 cases passed (164 ms)
# Your runtime beats 14.11 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

# 2. Dict
from functools import reduce
# Time: O(n)
# Space: O(n)
class Solution:
    def hasGroupsSizeX1(self, deck: List[int]) -> bool:
        def gcd(a, b):
            while b: 
                a, b = b, a % b
            return a
        count = collections.Counter(deck).values()
        return reduce(gcd, count) > 1

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck).values()
        res = 0
        for cnt in count:
            res = self.gcd(cnt, res)
        return res > 1

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

# 74/74 cases passed (144 ms)
# Your runtime beats 56.29 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().hasGroupsSizeX([1,2,3,4,4,3,2,1]))