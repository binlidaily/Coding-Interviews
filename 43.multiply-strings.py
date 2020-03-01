#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
# Time: O(nm)
# Space: O(n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ''
        if num1 == '0' or num2 == '0':
            return '0'
        str_int = dict(zip(list('0123456789')+['10', '11', '12', '13', '14', '15', '16', '17', '18'], range(19)))
        int_str = dict(zip(range(19), list('0123456789')+['10', '11', '12', '13', '14', '15', '16', '17', '18']))
        l1, l2 = len(num1), len(num2)
        res = ['0'] * (l1 + l2)
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                # this is crucial
                add = str_int[res[i + j + 1]] + str_int[num1[i]] * str_int[num2[j]]
                res[i + j + 1] = int_str[add % 10]
                res[i + j] = int_str[str_int[res[i + j]] + add // 10]
        l = len(res)
        for i in range(l):
            if res[i] != '0' or i == l - 1:
                return ''.join(res[i:])
        return ''

# 311/311 cases passed (132 ms)
# Your runtime beats 48.33 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().multiply(num1 = "2", num2 = "3"))
print(Solution().multiply(num1 = "123", num2 = "456"))
print(Solution().multiply(num1 = "999", num2 = "999"))