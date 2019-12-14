#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
import math
# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.k = k
    
        def backtrack(path, remain):
            if not remain:
                self.k -= 1
                if self.k == 0:
                    return path
                return ''
                
            for i in range(len(remain)):
                if self.k > math.factorial(len(remain)-1):
                    self.k -= math.factorial(len(remain)-1)
                    continue
                ans = backtrack(path + remain[i], remain[:i]+remain[i+1:])
                if ans: 
                    return ans
            return ''
        nums = list(map(str, range(1, n+1)))
        return backtrack('', nums)
# 200/200 cases passed (32 ms)
# Your runtime beats 78.87 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
        
# @lc code=end

print(Solution().getPermutation(3, 3))
print(Solution().getPermutation(9, 313531))