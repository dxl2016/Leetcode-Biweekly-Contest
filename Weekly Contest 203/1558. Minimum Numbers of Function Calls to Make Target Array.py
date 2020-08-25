class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        a = []
        for i in nums:
            if i == 1:
                ans += 1
            elif i == 0:
                continue
            else:
                a.append(i)
        nums = a
        curr_min = 2
        while(nums):
            q = []
            for each in nums:
                c, v = each//curr_min, each%curr_min
                ans += v
                if c == 1:
                    ans += 1
                elif c == 0:
                    continue
                else:
                    q.append(c)
            ans += 1
            nums = q
        
        return ans

