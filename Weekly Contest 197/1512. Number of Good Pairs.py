class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if not nums:
            return
        tmp = {}
        for k,v in enumerate(nums):
            if v not in tmp:
                tmp[v] = [k]
            else:
                tmp[v] += [k]
        ans = 0
        for each in tmp:
            ans += math.comb(len(tmp[each]), 2)
        
        return ans


