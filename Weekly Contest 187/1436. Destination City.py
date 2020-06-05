class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if not paths:
            return
        visited = set()
        temp = {}
        for i,j in paths:
            visited.add(i)
            visited.add(j)
            try:
                temp[i] += [j]
            except:
                temp[i] = [j]
        for items in visited:
            if items not in temp:
                return items
