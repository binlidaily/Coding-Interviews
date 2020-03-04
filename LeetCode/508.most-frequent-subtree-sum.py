#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#
from typing import List
import collections
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
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        hash_table = collections.defaultdict()
        self.subtree_sum(root, hash_table)
        max_cnt = max(hash_table.values())
        return [key for key in hash_table.keys() if hash_table[key] == max_cnt]

    def subtree_sum(self, root, hash_table):
        if not root:
            return 0
        if not root.left and not root.right:
            hash_table[root.val] = hash_table.get(root.val, 0) + 1
            return root.val
        sum_val = root.val + self.subtree_sum(root.left, hash_table) + self.subtree_sum(root.right, hash_table)
        hash_table[sum_val] = hash_table.get(sum_val, 0) + 1
        return sum_val

# 61/61 cases passed (44 ms)
# Your runtime beats 88.12 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (15.8 MB)

# @lc code=end

a = TreeNode(5)
l = TreeNode(2)
r = TreeNode(-3)
a.left = l
a.right = r
print(Solution().findFrequentTreeSum(a))

a = TreeNode(5)
l = TreeNode(2)
r = TreeNode(-5)
a.left = l
a.right = r
print(Solution().findFrequentTreeSum(a))