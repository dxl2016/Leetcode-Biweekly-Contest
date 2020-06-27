class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if not bloomDay:
            return []
        n = len(bloomDay)
        if n < m*k:
            return -1 
        L = sorted(set(bloomDay))
        for iter_day in L:
            a = ([n for n,i in enumerate(bloomDay) if i<=iter_day])
            if k == 1:
                if len(a) >= m:
                    return iter_day
            else:
                if len(a) >= m*k:
                    temp = []
                    c = 1
                    for i in range(1,len(a)):
                        if a[i]-a[i-1] == 1:
                            c += 1
                            if i==len(a)-1:
                                temp.append(c)
                        else:
                            temp.append(c)
                            c = 1
                    ans = m
                    for j in temp:
                        ans -= j//k
                        if ans<=0:
                            return iter_day

        return -1

