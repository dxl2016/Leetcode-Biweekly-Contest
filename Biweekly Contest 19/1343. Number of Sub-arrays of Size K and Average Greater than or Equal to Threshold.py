class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = [0]
        cusum = 0
        c = 0
        ans = 0
        for i,v in enumerate(arr):
            cusum += v
            res.append(cusum)
            if i+1 >=k:
                if cusum-res[i-k+1] >= threshold*k:
                    ans += 1
          
        return ans

