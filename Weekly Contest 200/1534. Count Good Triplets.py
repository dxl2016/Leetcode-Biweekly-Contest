class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(0, n-2):
            for l in range(i+1, n-1):
                for r in range(l+1, n):
                    if abs(arr[i]-arr[l]) <= a and abs(arr[l]-arr[r]) <= b and abs(arr[i]-arr[r]) <= c:
                        ans += 1
        
        return ans

