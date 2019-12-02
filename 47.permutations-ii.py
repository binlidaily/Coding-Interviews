#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
from typing import List
# @lc code=start
# Time: O(n^2)
# Space: O(n)
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         if not nums:
#             return []
#         res = []
#         nums.sort()
#         self.dfs(nums, [], res)
#         return res
    
#     def dfs(self, nums, path, res):
#         if not nums or len(nums) == 0:
#             res.append(path)
#         n = len(nums)
#         for i in range(n):
#             if i >= 1 and nums[i-1] == nums[i]:
#                 continue
#             self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
# # 30/30 cases passed (48 ms)
# # Your runtime beats 98.52 % of python3 submissions
# # Your memory usage beats 100 % of python3 submissions (12.8 MB)

# 2. iterative
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            tmp = []
            for item in res:
                for i in range(len(item)+1):
                    tmp.append(item[:i]+[n]+item[i:])
                    if i < len(item) and item[i] == n:
                        break
            res = tmp
        return res
# 30/30 cases passed (48 ms)
# Your runtime beats 98.52 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().permuteUnique([1,1,2]))
print(Solution().permuteUnique([3,3,0,3]))