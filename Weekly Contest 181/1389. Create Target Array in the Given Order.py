class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        l = []
        n = len(nums)
        for i in range(n):
            l.insert(index[i], nums[i])
        
        return l

