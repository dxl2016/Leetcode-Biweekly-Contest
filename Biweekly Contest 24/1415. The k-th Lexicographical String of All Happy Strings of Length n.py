class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if not n or not k:
            return
        
        temp = set()
        def recur(s, las_s, L):
            if L>n:
                temp.add(s[:-1])
                return
            if las_s == 'a':
                recur(s+'b', 'b', L+1)
                recur(s+'c', 'c', L+1)
            elif las_s == 'b':
                recur(s+'a', 'a', L+1)
                recur(s+'c', 'c', L+1)
            elif las_s == 'c':
                recur(s+'a', 'a', L+1)
                recur(s+'b', 'b', L+1) 
        
        recur('a', 'a', 1)
        recur('b', 'b', 1)
        recur('c', 'c', 1)
        
        temp = (sorted(temp))
        if len(temp) >= k:
            return temp[k-1]
        else:
            return ""
        
        
