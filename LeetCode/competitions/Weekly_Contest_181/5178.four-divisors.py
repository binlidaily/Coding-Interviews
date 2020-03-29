from typing import List
class Solution:
	def sumFourDivisors(self, nums: List[int]) -> int:
		if not nums:
			return 0
		res = 0
		for num in nums:
			divisors = self.countDivisors(num)
			print(divisors)
			if len(divisors) == 4:
				res += sum(divisors)
		return res

	def countDivisors1(self, num):
		return [i for i in range(1, num + 1) if num % i == 0]

print(Solution().sumFourDivisors([21,4,7]), 32)
print(Solution().sumFourDivisors([21,21]), 64)
