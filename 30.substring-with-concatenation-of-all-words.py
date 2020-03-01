#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
from typing import List
import collections
# @lc code=start
# Time: O(n^2)
# Space: O(n)
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         if not words:
#             return []
#         words_sz = len(words)
#         word_len = len(words[0])
#         s_len = len(s)

#         word_cnt = collections.defaultdict()
#         for word in words:
#             word_cnt[word] = word_cnt.get(word, 0) + 1
        
#         res = []
#         last_i = s_len - words_sz * word_len + 1

#         for i in range(last_i):
#             valid_cnt = 0
#             cur_cnt = collections.defaultdict()
#             last_j = i + words_sz * word_len

#             for j in range(i, last_j, word_len):
#                 word = s[j:j+word_len]
#                 if word not in word_cnt:
#                     continue
#                 cur_cnt[word] = cur_cnt.get(word, 0) + 1
#                 if cur_cnt[word] > word_cnt[word]:
#                     break
#                 valid_cnt += 1

#             if valid_cnt == words_sz:
#                 res.append(i)
#         return res


# 173/173 cases passed (600 ms)
# Your runtime beats 43.2 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)

# 2. Sliding window
# Time: O(n^2)
# Space: O(n)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        words_sz = len(words)
        word_len = len(words[0])

        word_cnt = collections.defaultdict()
        for word in words:
            word_cnt[word] = word_cnt.get(word, 0) + 1
        
        res = []

        for i in range(word_len):
            start = i
            cur_cnt = collections.defaultdict()
            last_j = len(s) - word_len + 1

            for j in range(i, last_j, word_len):
                word = s[j:j+word_len]
                if word in word_cnt:
                    cur_cnt[word] = cur_cnt.get(word, 0) + 1

                    while cur_cnt[word] > word_cnt[word]:
                        cur_cnt[s[start: start + word_len]] -= 1
                        start += word_len
                else:
                    cur_cnt.clear()
                    start = j + word_len

                if j - start == (words_sz-1) * word_len:
                    res.append(start)
        return res

# 173/173 cases passed (60 ms)
# Your runtime beats 95.13 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=end

print(Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))    # [0,9]
print(Solution().findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"])) # []
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))