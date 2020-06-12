class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if not nums:
            return
        ans = []
        cusum = 0
        for i in nums:
            cusum += i
            ans.append(cusum)
        
        x = min(ans)
        return max(-x+1, 1)
            
