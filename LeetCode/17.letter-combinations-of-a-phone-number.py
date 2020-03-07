#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (44.91%)
# Likes:    3215
# Dislikes: 368
# Total Accepted:    532.3K
# Total Submissions: 1.2M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# Example:
# 
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#

# @lc code=start
# Time: O(3^n)
# Space: O(n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is None or digits == '': 
            return []
        mapping = {'0':' ', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        self.dfs(mapping, digits, 0, '', res)
        return res
    
    def dfs(self, mapping, digits, level, cur, res):
        if level == len(digits):
            res.append(cur)
            return
        
        for c in mapping[digits[level]]:
            self.dfs(mapping, digits, level + 1, cur + c, res)

# 25/25 cases passed (24 ms)
# Your runtime beats 88.3 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

