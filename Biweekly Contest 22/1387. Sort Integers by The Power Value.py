class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        
        def calc(num):
            c = 0
            while(num>1):
                if num%2 == 0:
                    num //= 2
                else:
                    num = 3*num+1
                c += 1
            return c
        
        ans = set()
        for i in range(lo, hi+1):
            ans.add((i,calc(i)))
        # print(ans)
        ans = sorted(ans, reverse=False, key=lambda x:(x[1],x[0]))
        return ans[k-1][0]

