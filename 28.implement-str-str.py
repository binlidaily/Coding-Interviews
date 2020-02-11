#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
# Time: O(mn)
# Space: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        h = len(haystack)
        n = len(needle)
        if h < n:
            return -1
        for i in range(h - n + 1):
            if haystack[i] == needle[0]:
                idx = i
                j = 0
                while j < n:
                    if haystack[idx] != needle[j]:
                        break
                    j += 1
                    idx += 1
                if j == n:
                    return i
        return -1

# 74/74 cases passed (36 ms)
# Your runtime beats 37.85 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().strStr(haystack = "hello", needle = "ll"))
print(Solution().strStr(haystack = "aaaaa", needle = "bba"))
print(Solution().strStr(haystack = "aaa", needle = "aaaa"))
print(Solution().strStr(haystack = "mississippi", needle = "issipi"))
