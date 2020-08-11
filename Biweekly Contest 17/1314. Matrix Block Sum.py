class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = []
        
        def calc(i, j):
            res = 0
            for r in range(max(0, i-K), min(m, i+K+1)):
                for c in range(max(0, j-K), min(n, j+K+1)):
                    res += mat[r][c]
            return res

        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(calc(i, j))
            ans.append(tmp)
        
        return ans

