class Solution:
    def isPathCrossing(self, path: str) -> bool:
        if not path:
            return True
        ans = set()
        x, y = 0, 0
        ans.add((x,y))
        temp = {'N':[0,1], 'E':[1,0], 'W':[-1,0], 'S':[0,-1]}
        for s in path:
            x_i, y_i = temp[s]
            x += x_i
            y += y_i
            if (x,y) in ans:
                return True
            else:
                ans.add((x,y))
        
        return False

