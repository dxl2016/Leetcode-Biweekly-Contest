class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        ans = []
        for f,t in edges:
            if t not in graph:
                graph[t] = [f]
            else:
                graph[t].append(f)
        
        for x in range(n):
            if x not in graph:
                ans.append(x)
        
        return ans

