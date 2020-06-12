class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k == 1 or k == 2:
            return 1
        
        temp = [1, 1]
        def gen(k):
            a, b = 1, 1
            t = 0
            while(t<=k):
                t = a+b
                temp.append(t)
                a = b
                b = t
                
        gen(k)
        print(temp)
        i = len(temp)-2
        ans = 0
        diff = k
        while(True):
            diff = diff-temp[i]
            ans+=1
            if diff == 0:
                return ans
            i-=2
            while(diff<temp[i]):
                i-=1
            
            
            
