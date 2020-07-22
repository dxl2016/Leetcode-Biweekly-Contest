class Solution:
    def numSub(self, s: str) -> int:
        if not s:
            return 0
        if s.count("1") == 0:
            return 0
        tmp = []
        a = ""
        for i in s:
            if i == "0":
                tmp.append(a)
                a = ""
            else:
                a += "1"
        if a:
            tmp.append(a)
        if not tmp[0]:
            tmp = tmp[1:]
        
        ans = 0
        for each in tmp:
            n = len(each)
            ans += (1+n)*n//2
        
        return ans%(10**9+7)

