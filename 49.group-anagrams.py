#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
import collections
from typing import List
# @lc code=start
# Time: O(mnlogn)
# Time: O(nm)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = collections.defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in hash_map:
                hash_map[sorted_s].append(s)
            else:
                hash_map[sorted_s] = [s]
        return list(hash_map.values())

# 101/101 cases passed (92 ms)
# Your runtime beats 95.46 % of python3 submissions
# Your memory usage beats 96.23 % of python3 submissions (15.6 MB)
# @lc code=end

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))