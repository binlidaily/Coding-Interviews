#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#
from typing import List
import collections
# @lc code=start
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not start or not str or not bank:
            return -1
        queue = collections.deque()
        queue.append((start, 0))
        while queue:
            gene, step = queue.popleft()
            if gene == end:
                return step
            for i in range(len(gene)):
                for ch in 'ACGT':
                    new_gene = gene[:i] + ch + gene[i+1:]
                    if bank and new_gene in bank:
                        queue.append((new_gene, step + 1))
                        bank.remove(new_gene)
        return -1

# 14/14 cases passed (24 ms)
# Your runtime beats 86.19 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().minMutation(start = "AACCGGTT",
end = "AAACGGTA",
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))

print(Solution().minMutation("AACCGGTT",
"AACCGCTA",
["AACCGGTA","AACCGCTA","AAACGGTA"]))