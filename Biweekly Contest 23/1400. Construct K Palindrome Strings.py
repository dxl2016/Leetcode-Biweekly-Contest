class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        temp = {}
        for i in s:
            try:
                temp[i] += 1
            except:
                temp[i] = 1
        c_odd, c_even = 0, 0
        for items in temp:
            if temp[items]%2 == 1:
                c_odd += 1
                c_even += temp[items]//2
            else:
                c_even += temp[items]//2
            
        print(c_odd)
        print(c_even)
        
        if c_odd == k:
            return True
        if c_odd < k and c_odd+c_even >= k:
            return True
        if c_odd < k and c_odd+c_even*2 >= k:
            return True
        
        return False
    
    
