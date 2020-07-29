class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        stack = 0
        while(True):
            div = empty//numExchange
            ans += div
            empty -= div*numExchange
            stack += div
            empty += stack
            stack = 0
            if empty//numExchange == 0:
                break
        
        return ans

