#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        res = Lsum = Lmax = Msum = Mmax = 0
        n = len(A)
        # L left, M right
        for i in range(n):
            # add number value to M part
            Msum += A[i]
            # Keep M numbers
            if i - M >= 0:
                Msum -= A[i - M]
            # add number value to L part
            if i - M >= 0:
                Lsum += A[i - M]
            # Keep L numbers
            if i - M - L >= 0:
                Lsum -= A[i - M - L]
            # L find max, M move forward
            Lmax = max(Lmax, Lsum)
            res = max(res, Lmax + Msum)
        Lsum = Lmax = Msum = Mmax = 0
        # M left, L right
        for i in range(n):
            # add number to L part
            Lsum += A[i]
            # keep L numbers
            if i - L >= 0:
                Lsum -= A[i - L]
            if i - L >= 0:
                Msum += A[i - L]
            if i - L - M >= 0:
                Msum -= A[i - L - M]
            Mmax = max(Mmax, Msum)
            res = max(res, Mmax + Lsum)
        return res
# 51/51 cases passed (72 ms)
# Your runtime beats 37.21 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2))