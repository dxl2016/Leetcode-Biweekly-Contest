class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        temp = sorted(nums, reverse=False)
        tot = sum(temp)
        cusum = 0
        for k,i in enumerate(temp):
            cusum += i
            if cusum >= tot-cusum:
                return temp[k:][::-1]

