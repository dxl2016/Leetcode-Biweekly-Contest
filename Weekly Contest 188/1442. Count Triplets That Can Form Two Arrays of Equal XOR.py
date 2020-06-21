class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if not arr:
            return 0
        
        ans = []
        n = len(arr)
        for l in range(0, n):
            temp = arr[l]
            for r in range(l+1, n):
                temp ^= arr[r]
                if temp == 0:
                    ans.append((l,r))
       
        c = 0
        for first, second in ans:
            c += (second-first)
        
        return c

