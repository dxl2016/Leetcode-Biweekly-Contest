class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if not rating:
            return 0
        ans = 0
        n = len(rating)
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if rating[i] < rating[j] < rating[k]:
                        ans += 1
                    elif rating[i] > rating[j] > rating[k]:
                        ans += 1
        
        return ans

