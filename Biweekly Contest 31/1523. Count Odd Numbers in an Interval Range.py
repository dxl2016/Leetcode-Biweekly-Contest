class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = (high-low)//2
        if low%2 == 0 and high%2 == 0:
            return ans
        return ans+1

