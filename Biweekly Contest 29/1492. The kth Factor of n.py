class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        temp = set()
        l, r = 1, n
        while(l<=r):
            if n%l == 0:
                temp.add(l)
                r = n//l
                temp.add(r)
            l+=1
        if not temp:
            return -1
        else:
            ans = sorted(temp)
            if k>len(ans):
                return -1
            else:
                return ans[k-1]

