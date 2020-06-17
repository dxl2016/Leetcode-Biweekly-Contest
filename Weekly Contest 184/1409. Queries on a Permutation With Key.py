class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        if not queries:
            return
        counter = [i for i in range(m)]
        ans = []
        for p in queries:
            mid = counter[p-1]
            ans.append(mid)
            for idx in range(len(counter)):
                if counter[idx] < mid:
                    counter[idx] += 1
                elif counter[idx] == mid:
                    counter[idx] = 0
            
        return ans

