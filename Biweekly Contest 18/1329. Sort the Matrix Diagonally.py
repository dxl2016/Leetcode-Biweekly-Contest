class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        tot = m*n
        c_list = [i for i in range(n)] + [i*n for i in range(1, m)]
        # print(c_list)
        for each in c_list:
            res = []
            c = each
            while(c<tot):
                i, j = c//n, c%n
                res.append(mat[i][j])
                c += n+1
                if i == m-1 or j == n-1:
                    break
            res = sorted(res, reverse=True)
            # print(res)
            c = each
            while(res):
                i, j = c//n, c%n
                mat[i][j] = res.pop()
                c += n+1
                    
        return mat

