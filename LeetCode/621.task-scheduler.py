#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
import collections
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(n)
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         hash_map = collections.defaultdict()
#         for item in tasks:
#             hash_map[item] = hash_map.get(item, 0) + 1
#         values = list(hash_map.values())
#         max_v = max(values)
#         max_cnt = values.count(max_v)
#         return max(len(tasks), (max_v - 1) * (n + 1) + max_cnt)
# 64/64 cases passed (440 ms)
# Your runtime beats 64.19 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)

# Time: O(n)
# Space: O(n)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_cnts = collections.Counter(tasks).values()
        max_task_cnts = max(tasks_cnts)
        max_size = list(tasks_cnts).count(max_task_cnts)
        return max(len(tasks), (max_task_cnts - 1) * (n + 1) + max_size)
# 64/64 cases passed (440 ms)
# Your runtime beats 64.19 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

print(Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))