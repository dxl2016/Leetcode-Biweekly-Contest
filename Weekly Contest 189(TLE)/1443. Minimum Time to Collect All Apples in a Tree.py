class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if not edges or not hasApple:
            return 0
        graph = {}
        for i in range(n):
            graph[i] = []       
        for i,j in edges:
            try:
                graph[i] += [j]
            except:
                graph[i] = [j]
                
        self.ans = 0
        def dfs(node):
            self_or_children_apple = hasApple[node]
            for children in graph[node]:
                self_or_children_apple |= dfs(children)
            if self_or_children_apple and node>0:
                self.ans += 2
            
            return self_or_children_apple

        dfs(0)
        return self.ans
        
