class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tmp = {}
        for i in nums:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
        tmp = sorted(tmp.items(), key=lambda x:x[0])
        cum = 0
        res = []
        for each in tmp:
            res.append((each[0],cum))
            cum += each[1]
        res = dict(res)
        ans = []
        for i in nums:
            ans.append(res[i])
            
        return ans

