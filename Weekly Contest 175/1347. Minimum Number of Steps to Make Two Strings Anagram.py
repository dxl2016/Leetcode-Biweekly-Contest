class Solution:
    def minSteps(self, s: str, t: str) -> int:
        tmp = {}
        for i in s:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
        ans = 0
        for j in t:
            if j in tmp and tmp[j]>0:
                tmp[j] -= 1
            else:
                ans += 1
        
        return ans

