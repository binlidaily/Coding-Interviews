# -*- coding:utf-8 -*-
# Time: O(mn)
# Space: O(mn)
class Backpack:
    def maxValue(self, w, v, n, cap):
        dp = [[0 for _ in range(cap + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, cap + 1):
                if w[i-1] <= j:
                    dp[i][j] = max(dp[i - 1][j - w[i-1]] + v[i-1], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][cap]

print(Backpack().maxValue([1,2,3],[1,2,3],3,6)) # 6