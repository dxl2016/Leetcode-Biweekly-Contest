class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        def helper(n):
            count = set()
            for i in range(1, int(n**0.5)+1):
                if n%i == 0:
                    count.add(i)
                    count.add(n//i)
                    # print(count)
                if len(count)>4:
                    return 0
            
            return sum(count) if len(count) == 4 else 0
            
        ans = 0
        for items in nums:
            ans += helper(items)
        return ans

