class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        t = {}
        for (i,v) in enumerate(arr):
            if v not in t:
                t[v] = [i]
            else:
                t[v] += [i]
        t = sorted(t.items())
        # print(t)
        ans = [0]*len(arr)
        c = 1
        for _, seq in t:
            for each in seq:
                ans[each] = c
            c += 1
            
        return ans

