#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
# Time: O(n)
# Sapce: O(1)
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n > 1:
#             while n % 3 == 0: 
#                 n /= 3
#         return n == 1

# 21038/21038 cases passed (56 ms)
# Your runtime beats 98.46 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)

# Time: O(n)
# Sapce: O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

# 21038/21038 cases passed (72 ms)
# Your runtime beats 75.88 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().isPowerOfThree(27))    # True
print(Solution().isPowerOfThree(0))    # False
print(Solution().isPowerOfThree(45))    # False
print(Solution().isPowerOfThree(9))    # True
print(Solution().isPowerOfThree(1))    # True