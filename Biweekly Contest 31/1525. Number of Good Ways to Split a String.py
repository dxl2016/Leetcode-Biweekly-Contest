class Solution:
    def numSplits(self, s: str) -> int:
        ans = 0
        a, b = [], collections.Counter(s)
        l1, l2 = 0, len(b)
        
        for i in s:
            if i not in a:
                a += [i]
                l1 += 1
            
            if i in b and b[i] > 0:
                b[i] -= 1
                if b[i] == 0:
                    l2 -= 1
            
            if l1 == l2:
                ans += 1
        
        return ans

