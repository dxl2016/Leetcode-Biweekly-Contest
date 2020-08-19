class Solution:
    def makeGood(self, s: str) -> str:
        i = 1
        while(i<len(s)):
            if s[i] != s[i-1] and (s[i].upper() == s[i-1] or s[i].lower() == s[i-1]):
                if i+1<len(s):
                    s = s[:i-1]+s[i+1:]
                else:
                    s = s[:i-1]
                # print(s)
                i = 1
            else:
                i += 1
                
        return s
  
  
