class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        cu_sum = 0
        arr = sorted(arr)
        tmp = set()
        for i in arr:
            cu_sum += i
            tmp.add(cu_sum)
            
            for k in tmp:
                if (cu_sum-k)%2 == 1:
                    ans += 1
                    
        return ans%(10**9+7)


    
