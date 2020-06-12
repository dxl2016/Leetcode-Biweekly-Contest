class Solution:
    def reformat(self, s: str) -> str:
        if not s:
            return
        dict_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        a, b = [], []
        for items in s:
            if items in dict_digits:
                a.append(items)
            else:
                b.append(items)
        ans = ""
        if abs(len(a)-len(b))>1:
            return ""
        if (not a and len(b) == 1):
            return b[0]
        elif (not b and len(a) == 1):
            return a[0]
        elif (not a and len(b) > 1):
            return ""
        elif (not a and len(b) > 1):
            return ""
        
        if len(a)>len(b):
            while(b):
                ans += a.pop(0)
                ans += b.pop(0)
            ans += a.pop(0)    
        elif len(a)<len(b):
            while(a):
                ans += b.pop(0)
                ans += a.pop(0)
            ans += b.pop(0)
        else:
            while(a):
                ans += b.pop(0)
                ans += a.pop(0)
        return ans
        
        
