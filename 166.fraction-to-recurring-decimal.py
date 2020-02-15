#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#
import collections
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        # hash_map store the index
        hash_map = collections.defaultdict()
        res = '-' if (numerator > 0) ^ (denominator > 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        div, mod = divmod(numerator, denominator)
        if mod == 0:
            return res + str(div)
        res += str(div) + '.'
        hash_map[mod] = len(res)
        while mod:
            mod *= 10
            div, mod = divmod(mod, denominator)
            res += str(div)
            if mod in hash_map:
                idx = hash_map[mod]
                res = res[:idx] + '(' + res[idx:] + ')'
                break
            else:
                hash_map[mod] = len(res)
        return res

# 37/37 cases passed (28 ms)
# Your runtime beats 69.35 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

