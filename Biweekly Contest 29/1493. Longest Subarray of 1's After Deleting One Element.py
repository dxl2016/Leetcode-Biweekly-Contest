class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums or sum(nums) == 0:
            return 0
        if sum(nums) == len(nums):
            return len(nums)-1
        
        temp = []
        c = 0
        idx = 0
        for k,v in enumerate(nums):
            if v == 1:
                c += 1
            else:
                if c>0:
                    temp.append([idx, c])
                c = 0
                idx = k+1
        if c>0:
            temp.append((len(nums)-c, c))
        temp = sorted(temp, reverse=False, key=lambda x:x[0])
        print(temp)
        cur_max = temp[0][1]
        for j in range(1, len(temp)):
            if temp[j][0]-(temp[j-1][0]+temp[j-1][1]) == 1:
                cur_max = max(cur_max, temp[j][1]+temp[j-1][1])
            else:
                cur_max = max(cur_max, temp[j][1])
        
        return cur_max

