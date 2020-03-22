from typing import List
class Solution:
	def longestPrefix1(self, s: str) -> str:
		prefix, suffix = [], []
		n = len(s)
		res = []
		for i in range(n-1):
			prefix.append(s[i])
			suffix.insert(0, s[n-1-i])
			print(prefix, suffix)
			if prefix == suffix:
				res = prefix
		return ''.join(res)

	def longestPrefix(self, s: str) -> str:
		prefix, suffix = '', ''
		n = len(s)
		res = ''
		for i in range(n-1):
			prefix = prefix + s[i]
			suffix = s[n-1-i] + suffix

			if prefix == suffix:
				res = prefix
		return ''.join(res)

print(Solution().longestPrefix(s = "ababab"))