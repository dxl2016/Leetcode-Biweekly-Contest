class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        
        ans = 0
        temp = 0
        curr_min = curr_max = nums[0]
        curr_min_idx = curr_max_idx = 0
        for i in range(len(nums)):
            if nums[i] <= curr_min:
                curr_min = nums[i]
                curr_min_idx = i
            if nums[i] >= curr_max:
                curr_max = nums[i]
                curr_max_idx = i
            if abs(curr_min-curr_max) <= limit:
                temp += 1
            else:
                ans = max(ans, temp)
                i = min(curr_min_idx, curr_max_idx)
                temp = 0
                curr_min = curr_max = nums[i+1]
                curr_min_idx = curr_max_idx = i+1
        
        return max(ans, temp)
                
        
        
