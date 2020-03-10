#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (55.26%)
# Likes:    1866
# Dislikes: 183
# Total Accepted:    353.4K
# Total Submissions: 638.7K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
from typing import List
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, l, r):
        if l > r:
            return None
        mid = l + ((r - l) >> 1)
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, l, mid - 1)
        root.right = self.dfs(nums, mid + 1, r)
        return root

# 32/32 cases passed (64 ms)
# Your runtime beats 97.52 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (15.1 MB)
# @lc code=end

