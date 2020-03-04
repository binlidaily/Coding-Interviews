#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# 476/476 cases passed (48 ms)
# Your runtime beats 61.55 % of python3 submissions
# Your memory usage beats 76.19 % of python3 submissions (13.3 MB)

# @lc code=end

print(Solution().isPalindrome("race a car"))    # False
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))    # True
print(Solution().isPalindrome("0P"))    # False