class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        ans = [False]*n
        max_candies = max(candies)
        for i,j in enumerate(candies):
            if j+extraCandies >= max_candies:
                ans[i] = True
        return ans
