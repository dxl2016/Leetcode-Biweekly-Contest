class Solution:
    def sortString(self, s: str) -> str:
        tmp = {}
        for i in s:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
        tmp = sorted(tmp.items(), key=lambda x:x[0])
        print(tmp)
        k = [items[0] for items in tmp]
        v = [items[1] for items in tmp]
        n = len(tmp)
        
        ans = ""
        x = 0
        while(len(ans) != len(s)):
            c = ""
            for i in range(n):
                if v[i] > 0:
                    v[i] -= 1
                    c += k[i]
            if x%2 == 0:
                ans += c
            else:
                ans += c[::-1]
            x += 1
        
        return ans

