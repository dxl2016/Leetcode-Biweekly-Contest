class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        ans = []
        cusum = 0
        for i in nums:
            cusum += i
            ans.append(cusum)
        
        return ans
