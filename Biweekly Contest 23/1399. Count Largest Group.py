class Solution:
    def countLargestGroup(self, n: int) -> int:
        if not n:
            return 0
        temp = {}
        for i in range(1, n+1):
            if i <= 9:
                a = i
            else:
                a = 0
                for s in str(i):
                    a += int(s)
            try:
                temp[a] += 1
            except:
                temp[a] = 1
        
        return len({k:v for (k,v) in temp.items() if v == max(temp.values())})
