class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if not cardPoints:
            return 0
        
        n = len(cardPoints)
        diff = n-k
        if k == n:
            return sum(cardPoints)
        curr_min = float('Inf')
        temp = sum(cardPoints[:diff])
        curr_min = temp
        i = diff
        while(i<n):
            temp = temp+cardPoints[i]-cardPoints[i-diff]
            curr_min = min(curr_min, temp)
            i += 1
        return sum(cardPoints) - curr_min
        
        
        
#         n = len(cardPoints)   
#         dp = [[0 for i in range(k+1)] for j in range(k+1)]
#         curr_max = 0
#         for l in range(k+1):
#             for r in range(k+1):
#                 if l+r <= k:
#                     if l == 0 and r > 0:
#                         dp[l][r] = sum(cardPoints[n-r:])
#                     elif l > 0 and r == 0:
#                         dp[l][r] = sum(cardPoints[:l])
#                     else:
#                         dp[l][r] = max(dp[l-1][r]+cardPoints[l-1], dp[l][r-1]+cardPoints[-r])
        
#                     if l+r == k:
#                         curr_max = max(curr_max, dp[l][r])
        
#         return curr_max
