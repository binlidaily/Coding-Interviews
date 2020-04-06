# Wrong Answer
# https://leetcode-cn.com/contest/weekly-contest-183/problems/longest-happy-string/
# 输入：
# 4 4 3
# 输出：
# "aabbbaccabc"
# 预期：
# "aabbccaabbc"

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_v = max(a, b, c)
        if max_v == 0:
            return ''
        elif max_v < 3:
            return a * 'a' + b * 'b' + c * 'c'
        if max_v == a:
            if b > 0:
                return 2 * 'a' + 1 * 'b' + self.longestDiverseString(a-2, b-1, c)
            if c > 0:
                return 2 * 'a' + 1 * 'c' + self.longestDiverseString(a-2, b, c-1)
            if b == 0 and c == 0:
                if a >= 2:
                    return 2 * 'a'
                else:
                    return max_v * 'a'
        elif max_v == b:
            if a > 0:
                return 2 * 'b' + 1 * 'a' + self.longestDiverseString(a-1, b-2, c)
            if c > 0:
                return 2 * 'b' + 1 * 'c' + self.longestDiverseString(a, b-2, c-1)
            if a == 0 and c == 0:
                if b >= 2:
                    return 2 * 'b'
                else:
                    return max_v * 'b'
        elif max_v == c:
            if a > 0:
                return 2 * 'c' + 1 * 'a' + self.longestDiverseString(a-1, b, c-2)
            if b > 0:
                return 2 * 'c' + 1 * 'b' + self.longestDiverseString(a, b-1, c-2)
            if a == 0 and b == 0:
                if c >= 2:
                    return 2 * 'c'
                else:
                    return max_v * 'c'

print(Solution().longestDiverseString(a = 1, b = 1, c = 7), "ccaccbcc", Solution().longestDiverseString(a = 1, b = 1, c = 7) == "ccaccbcc")
print(Solution().longestDiverseString(a = 2, b = 2, c = 1), "aabbc", Solution().longestDiverseString(a = 2, b = 2, c = 1) == "aabbc")
print(Solution().longestDiverseString(a = 7, b = 1, c = 0), "aabaa", Solution().longestDiverseString(a = 7, b = 1, c = 0) == "aabaa")