#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (30.62%)
# Likes:    1618
# Dislikes: 524
# Total Accepted:    313.5K
# Total Submissions: 1M
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#

# @lc code=start
# Time: O(nloglogn)
# Space: O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        tags = [True for _ in range(n)]
        tags[0], tags[1] = False, False
        sqrtn = int(round(n ** 0.5))
        for i in range(2, sqrtn + 1):
            if tags[i]:
                for j in range(i * i, n, i):
                    tags[j] = False
        
        return sum(tags)
# 20/20 cases passed (500 ms)
# Your runtime beats 63.22 % of python3 submissions
# Your memory usage beats 62.07 % of python3 submissions (27.6 MB)
# @lc code=end

