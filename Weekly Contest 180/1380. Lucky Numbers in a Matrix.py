class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return 0
        ans = {}
        a = [0 for _ in range(len(matrix[0]))]
        for items in matrix:
            min_val = float('Inf')
            min_idx = None
            for k,v in enumerate(items):
                a[k] = max(a[k], v)
                if v < min_val:
                    min_val = v
                    min_idx = k
            if min_idx not in ans:
                ans[min_idx] = [min_val]
            else:
                ans[min_idx] += [min_val]
        print(ans)
        print(a)
        result = []
        for items in ans:
            for j in ans[items]:
                if j == a[items]:
                    result.append(j)
        return result

