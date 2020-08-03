class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for k,v in enumerate(manager):
            if v != -1:
                graph[v].append(k)
        # print(graph)
        
        def dfs(node, t):
            self.ans = max(t, self.ans)
            for neigh in graph[node]:
                
                dfs(neigh, t+informTime[neigh])
            
            
        self.ans = 0
        dfs(headID, informTime[headID])
        
        return self.ans

