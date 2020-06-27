class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        def helper(n):
            count = set()
            l, r = 2, n
            while(l<r):
                if n%l == 0:
                    # print(l)
                    r = n//l
                    count.add(l)
                    count.add(r)
                l += 1
                if len(count)>2:
                    return 0
            
            return sum(count)+1+n if len(count) == 2 else 0
            
        ans = 0
        for items in nums:
            ans += helper(items)
        return ans

