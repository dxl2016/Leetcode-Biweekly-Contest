class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if not grid:
            return True
        
        def dfs(v, h):
            # print((v,h))
            visited.add((v,h))
            if v == m-1 and h == n-1:
                self.ans = True
                return
            
            if grid[v][h] == 1:
                if (h-1>=0):
                    if grid[v][h-1] in [1,4,6] and (v,h-1) not in visited:
                        dfs(v, h-1)
                if (h+1<n):
                    if grid[v][h+1] in [1,3,5] and (v,h+1) not in visited:
                        dfs(v, h+1)
            elif grid[v][h] == 2:
                if (v-1>=0):
                    if grid[v-1][h] in [2,3,4] and (v-1,h) not in visited:
                        dfs(v-1, h)
                if (v+1<m):
                    if grid[v+1][h] in [2,5,6] and (v+1,h) not in visited:
                        dfs(v+1, h)
            elif grid[v][h] == 3:
                if (h-1>=0):
                    if grid[v][h-1] in [1,4,6] and (v,h-1) not in visited:
                        dfs(v, h-1)
                if (v+1<m):
                    if grid[v+1][h] in [2,5,6] and (v+1,h) not in visited:
                        dfs(v+1, h)
            elif grid[v][h] == 4:
                if (h+1<n):
                    if grid[v][h+1] in [1,3,5] and (v,h+1) not in visited:
                        dfs(v, h+1)
                if (v+1<m):
                    if grid[v+1][h] in [2,5,6] and (v+1,h) not in visited:
                        dfs(v+1, h)
            elif grid[v][h] == 5:
                if (h-1>=0):
                    if grid[v][h-1] in [1,4,6] and (v,h-1) not in visited:
                        dfs(v, h-1)
                if (v-1>=0):
                    if grid[v-1][h] in [2,3,4] and (v-1,h) not in visited:
                        dfs(v-1, h)
            elif grid[v][h] == 6:
                if (h+1<n):
                    if grid[v][h+1] in [1,3,5] and (v,h+1) not in visited:
                        dfs(v, h+1)
                if (v-1>=0):
                    if grid[v-1][h] in [2,3,4] and (v-1,h) not in visited:
                        dfs(v-1, h)
       
        visited = set()
        m, n = len(grid), len(grid[0])
        self.ans = False
        dfs(0, 0)
        return self.ans

