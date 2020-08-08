class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s)
        ans = 0
        tmp = {}
        for i in range(n):
            if s[i] == t[i]:
                continue
            else:
                c = ord(t[i])-ord(s[i])
                if c<0:
                    c = 26+c
                # print(c)
                if c>k:
                    return False
                if c not in tmp:
                    tmp[c] = (k-c)//26
                else:
                    if tmp[c]>0:
                        tmp[c] -= 1
                    else:
                        return False
        
        return True

