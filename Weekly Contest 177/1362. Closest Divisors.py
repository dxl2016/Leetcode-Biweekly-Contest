class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for k in range(int(math.sqrt(num+2)), 0, -1):
            for final in (num+1, num+2):
                if final%k == 0:
                    return final//k, k

