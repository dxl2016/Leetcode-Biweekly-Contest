class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n%2 == 0:
            res = n//2
        else:
            res = n//2+1
        tmp = {}
        for i in arr:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
        tmp = sorted(tmp.items(), reverse=True, key=lambda x:x[1])
        ans = 0
        for each in tmp:
            n -= each[1]
            ans += 1
            if n<=res:
                return ans

