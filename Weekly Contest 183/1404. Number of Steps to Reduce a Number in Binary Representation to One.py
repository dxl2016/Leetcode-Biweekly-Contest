class Solution:
    def numSteps(self, s: str) -> int:
        s_int = int(s, 2)
        ans = 0
        while(s_int != 1):
            if s_int%2 == 1:
                s_int += 1
                ans += 1
            else:
                s_int //= 2
                ans += 1
        return ans

