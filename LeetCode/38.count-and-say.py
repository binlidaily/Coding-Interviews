#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
# Time: O(n^2)
# Space: O(n)
class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0:
            return ''
        res = '1'
        if n == 1:
            return '1'
        for i in range(n-1):
            res = self.count_read(res)
        return res
    
    def count_read(self, strs):
        if not strs:
            return ''
        n = len(strs)
        if n == 1:
            return '1'+ strs
        cnt = 1
        res = ''
        for i in range(n):
            if i >= 1 and strs[i-1] == strs[i]:
                cnt += 1
            elif i >= 1 and strs[i-1] != strs[i]:
                res += str(cnt) + strs[i-1]
                cnt = 1
            if i == n-1:
                if cnt == 1:
                    res += '1' + strs[i]
                else:
                    res += str(cnt) + strs[i]
        return res
# 18/18 cases passed (36 ms)
# Your runtime beats 84.12 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)



# @lc code=end

print(Solution().countAndSay(4))