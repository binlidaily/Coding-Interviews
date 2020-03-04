#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
from typing import List
# @lc code=start
# Time: O(mn*min(m,n))
# Space: O(n)
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0
#         r, c = len(matrix), len(matrix[0])
#         max_area = 0
#         for i in range(r):
#             for j in range(c):
#                 for l in range(min(r, c)):
#                     if self.check_square(matrix, i, j, i + l, j + l):
#                         max_area = max(max_area, (l+1)**2)
#         return max_area
    
#     def check_square(self, matrix, x, y , bottom_x, bottom_y):
#         r, c = len(matrix), len(matrix[0])
#         if bottom_x >= r or bottom_y >= c:
#             return False
#         for i in range(x, bottom_x+1):
#             for j in range(y, bottom_y+1):
#                 if matrix[i][j] == '0':
#                     return False
#         return True
# Time Limit Exceeded
# 69/69 cases passed (N/A)

# 2. DP
# TODO
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0
#         r, c = len(matrix), len(matrix[0])
#         # dp_area = [[1 if matrix[i][j] == '1' else 0 for j in range(c)] for i in range(r)]
#         dp_area = [[0 for _ in range(c)] for _ in range(r)]
#         # dp_area[0][0] = 1 if matrix[0][0] == '1' else 0
#         for i in range(r):
#             dp_area[i][0] = 1 if matrix[i][0] == '1' else 0
#         for i in range(c):
#             dp_area[0][i] = 1 if matrix[0][i] == '1' else 0
#         for i in range(1, r):
#             for j in range(1, c):
#                 dp_area[i][j] = dp_area[i-1][j] + dp_area[i][j-1] - dp_area[i-1][j-1] + int(matrix[i][j])
#         max_area = 0
#         for i in range(r):
#             for j in range(c):
#                 for l in range(min(r-i, c-j)-1, -1, -1):
#                     area = dp_area[i+l][j+l] - dp_area[i+l][j] - dp_area[i][j+l] + dp_area[i][j]
#                     print(area, l, (l+1) ** 2)
#                     if area == (l+1) ** 2:
#                         max_area = max(max_area, area)
#                         break
#         return max_area

# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0
#         r, c = len(matrix), len(matrix[0])
#         dp_area = [[0 for _ in range(c+1)] for _ in range(r+1)]
#         for i in range(1, r+1):
#             for j in range(1, c+1):
#                 dp_area[i][j] = dp_area[i-1][j] + dp_area[i][j-1] - dp_area[i-1][j-1] + int(matrix[i-1][j-1])
#         max_area = 0
#         for i in range(1, r+1):
#             for j in range(1, c+1):
#                 for l in range(min(r-i, c-j)+1, 0, -1):
#                     area = dp_area[i+l-1][j+l-1] - dp_area[i+l-1][j-1] - dp_area[i-1][j+l-1] + dp_area[i-1][j-1]
#                     if area == l ** 2:
#                         max_area = max(max_area, area)
#                         break
#         return max_area

# Time: O(mn)
# Space:O(mn)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m , n = len(matrix), len(matrix[0])
        dp = [[ 0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
        
        res = max(max(row) for row in dp)
        return res ** 2

# 69/69 cases passed (200 ms)
# Your runtime beats 73.57 % of python3 submissions
# Your memory usage beats 81.82 % of python3 submissions (13.9 MB)


# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0
        
#         dp = [0 if c == '0' else 1 for c in matrix[0]]
#         res = max(dp)
#         for i in range(1,len(matrix)):
#             pre = dp[0]
#             dp[0] = 0 if matrix[i][0] == '0' else 1
#             for j in range(1,len(matrix[0])):
#                 if matrix[i][j] == '1':
#                     dp[j], pre = min(dp[j-1], dp[j], pre)+1, dp[j]
#                 else:
#                     pre, dp[j] = dp[j], 0
                    
#             res = max(max(dp), res)
            
#         return res ** 2

# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         rows, maxSize = len(matrix), 0
#         if rows>0:
#             cols = len(matrix[0])
#             size = [0]*cols
#             for x in range(rows):
#                 count, size = 0, list(map(lambda x,y: x+1 if y=="1" else 0, size, matrix[x]))
#                 for y in range(cols):
#                     if size[y]>maxSize:
#                         count += 1
#                         if count > maxSize:
#                             maxSize += 1
#                             break
#                     else:
#                         count = 0
#         return maxSize**2

# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         n = len(matrix)
        
#         if n == 0:
#             return 0
        
#         m = len(matrix[0])
#         if m == 0:
#             return 0
        
#         dp = [[0] * m for _ in range(n)]
#         maxim = 0
#         for i in range(n):
#             for j in range(m):
#                 if i == 0 or j == 0:
#                     if matrix[i][j] == "1":
#                         dp[i][j] = 1
#                 else:
#                     if matrix[i][j] == "1":
#                         dp[i][j] = 1 + min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
#                     else:
#                         dp[i][j] = 0
#                 if dp[i][j] > maxim:
#                     maxim = dp[i][j]
#         return maxim * maxim

# @lc code=end

print(Solution().maximalSquare([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]]))
# 4
print(Solution().maximalSquare(['0']))
print(Solution().maximalSquare(['1']))