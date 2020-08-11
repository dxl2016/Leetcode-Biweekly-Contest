class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)//2
        for i in range(n):
            freq, val = nums[2*i], nums[2*i+1]
            ans += [val]*freq
        
        return ans

