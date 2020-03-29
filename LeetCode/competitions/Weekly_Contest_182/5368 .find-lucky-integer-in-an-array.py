from typing import List
import collections

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map = collections.defaultdict()
        for num in arr:
            hash_map[num] = hash_map.get(num, 0) + 1
        res = []
        for key, val in hash_map.items():
            if key == val:
                res.append(key)
        return max(res) if res else -1


print(Solution().findLucky(arr = [2,2,3,4]), 2)
print(Solution().findLucky(arr = [1,2,2,3,3,3]), 3)
print(Solution().findLucky(arr = [2,2,2,3,3]), -1)
print(Solution().findLucky(arr = [5]), -1)
print(Solution().findLucky(arr = [7,7,7,7,7,7,7]), 7)