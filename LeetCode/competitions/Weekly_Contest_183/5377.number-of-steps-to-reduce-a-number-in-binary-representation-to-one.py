class Solution:
    def numSteps(self, s: str) -> int:
        dec, is_odd = self.bin2dec(s)
        cnt = 0
        while dec != 1:
            if is_odd:
                dec += 1
            else:
                dec //= 2
            is_odd = dec % 2
            cnt += 1
        return cnt

    def bin2dec(self, s):
        dec = 0
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                dec += 2 ** (n-1-i)
        return dec, dec % 2

print(Solution().numSteps(s = "10"), 1)
print(Solution().numSteps(s = "1101"), 6)
print(Solution().numSteps(s = "1"), 0)