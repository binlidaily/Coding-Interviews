from typing import List
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n <= 2:
            return 0
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        res += 1
        return res



print(Solution().numTeams(rating = [2,5,3,4,1]), 3)
print(Solution().numTeams(rating = [2,1,3]), 0)
print(Solution().numTeams(rating = [1,2,3,4]), 4)