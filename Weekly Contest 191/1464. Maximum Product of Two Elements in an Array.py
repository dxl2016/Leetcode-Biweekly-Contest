class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        temp = sorted(nums, reverse=True)
        return int((temp[0]-1)*(temp[1]-1))
        
