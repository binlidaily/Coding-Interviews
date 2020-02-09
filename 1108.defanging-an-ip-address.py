#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
#

# @lc code=start
# Time: O(n)
# Space: O(1)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        arr = list(address)
        n = len(arr)
        for i in range(n):
            if arr[i] == '.':
                arr[i] = '[.]'
        return ''.join(arr)
# 62/62 cases passed (28 ms)
# Your runtime beats 57.53 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

print(Solution().defangIPaddr("1.1.1.1"))