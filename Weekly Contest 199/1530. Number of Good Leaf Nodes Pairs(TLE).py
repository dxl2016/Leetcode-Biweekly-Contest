# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = collections.defaultdict(list)
        leaf = []
        
        def dfs(node, par = None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)
                
                if node and not node.left and not node.right:
                    leaf.append(node)
        
        def bfs(node, target, c):
            if c <= distance:
                if node == target:
                    if c <= distance:
                        self.ans += 1
                    return

                seen.add(node)
                for neigh in graph[node]:
                    if neigh not in seen:
                        bfs(neigh, target, c+1)
        
        dfs(root)
        # print(graph)
        # print(leaf)
        n = len(leaf)
        
        self.ans = 0
        for i in range(0,n-1):
            for j in range(i+1,n):
                seen = set()
                bfs(leaf[i], leaf[j], 0)
            
        return self.ans

