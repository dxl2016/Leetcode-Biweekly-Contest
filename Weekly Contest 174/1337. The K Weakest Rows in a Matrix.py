class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for idx,each in enumerate(mat):
            c = 0
            for i in each:
                if i == 1:
                    c += 1
                else:
                    break
            res.append([c,idx])
        res = sorted(res)
        
        return [res[x][1] for x in range(k)]

