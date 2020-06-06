class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if not nums:
            return
        temp = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                try:
                    temp[i+j] += [nums[i][j]]
                except:
                    temp[i+j] = [nums[i][j]]
        ans = []
        for items in temp:
            ans += temp[items][::-1]
        return ans
        
