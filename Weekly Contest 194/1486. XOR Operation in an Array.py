class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        i = 1
        while(i<n):
            start += 2
            ans ^= start
            i += 1
            
        return ans

