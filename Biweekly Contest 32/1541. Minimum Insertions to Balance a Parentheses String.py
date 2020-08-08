class Solution:
    def minInsertions(self, s: str) -> int:
        q_c = 0
        ans = 0
        n = len(s)
        i = 0
        while(i<n):
            if s[i] == "(":
                q_c += 1
                i += 1
            else:
                if q_c>0:
                    q_c -= 1
                    if i+1<n and s[i+1] == ")":
                        i += 2
                    elif i+1<n and s[i+1] == "(":
                        i += 1
                        ans += 1
                    else:
                        i += 1
                        ans += 1
                else:
                    if i+1<n and s[i+1] == ")":
                        ans += 1
                        i += 2
                    else:
                        ans += 2
                        i += 1
                        
        if q_c>0:
            ans += q_c*2
        return ans

