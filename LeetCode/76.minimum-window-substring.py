#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
import collections
# @lc code=start
# Time: O(n)
# Space: O(n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map = collections.defaultdict(int)
        for ch in t:
            hash_map[ch] += 1
        # hash_map = collections.Counter(t)
        l, r = 0, 0
        min_window = ''
        cnt = len(t)
        
        for r in range(len(s)):
            # If we see a target letter, decrease the total target letter count
            if hash_map[s[r]] > 0:
                cnt -= 1
            
            # Decrease the letter count for the current letter
			# If the letter is not a target letter, the count just becomes -ve
            hash_map[s[r]] -= 1

            # If all letters in the target are found:
            while cnt == 0:
                win_size = r - l + 1
                if not min_window or win_size < len(min_window):
                    # Note the new minimum window
                    min_window = s[l:r+1]
                # Increase the letter count of the current letter
                hash_map[s[l]] += 1

                # If all target letters have been seen and now, a target letter is seen with count > 0
				# Increase the target length to be found. This will break out of the loop
                if hash_map[s[l]] > 0:
                    cnt += 1
                l += 1
        return min_window

# 268/268 cases passed (88 ms)
# Your runtime beats 92.35 % of python3 submissions
# Your memory usage beats 61.11 % of python3 submissions (13.4 MB)
# @lc code=end

print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))