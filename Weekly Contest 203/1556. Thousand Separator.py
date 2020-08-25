class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        if len(s) <= 3:
            return s
        ans = []
        c = 0
        for i in range(len(s)-1, -1, -1):
            ans.append(s[i])
            c += 1
            if c == 3:
                ans.append(".")
                c = 0
        if ans[-1] == ".":
            ans = ans[:-1]
        
        return "".join(ans[::-1])

