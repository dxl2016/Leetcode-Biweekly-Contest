class Solution:
    def removeCoveredIntervals(self, c: List[List[int]]) -> int:
        if not c:
            return 0
        n = len(c)
        c = sorted(c, key=lambda x:(x[0],-x[1]))
        # print(c)
        ans = n
        l, r = c[0][0], c[0][1]
        for (i,j) in c[1:]:
            if l<=i and r>=j:
                ans -= 1
            else:
                l, r = i, j
        
        return ans

