#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
from typing import List
# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) < 4:
            return []
        
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        if path and s == '' and len(path) == 4:
            res.append('.'.join(path))
            return
        
        if path and len(path) > 4:
            return
        
        for i in range(3):
            if i < len(s) and int(s[:i+1]) <= 255:
                if s[:i+1].startswith('0') and i >= 1:
                    continue
                self.dfs(s[i+1:], path+[s[:i+1]], res)

# 147/147 cases passed (32 ms)
# Your runtime beats 87.3 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

print(Solution().restoreIpAddresses('25525511135'))
print(Solution().restoreIpAddresses('010010'))