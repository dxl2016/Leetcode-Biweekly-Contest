class Solution:
    def minFlips(self, target: str) -> int:
        if not target:
            return
        
        ans = 0
        c = 0
        n = len(target)
        for i in target:
            if i == "0":
                c += 1
            else:
                break
        if c == n:
            return 0
        tmp = target[c:]
        for k,v in enumerate(tmp):
            if v == "0" and tmp[k-1] == "1":
                ans += 1

        if tmp[-1] == "0":
            return ans*2
        
        return ans*2+1

