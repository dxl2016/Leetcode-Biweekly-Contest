# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return
        
        def dfs(node, direction, c, parent):
            if not node:
                self.ans = max(self.ans, c-1)
                return
            
            # self.ans = max(self.ans, c)
            if direction == 0:
                dfs(node.right, 1, c+1, node)
                if parent:
                    dfs(node.left, 0, 1, node)
            if direction == 1:
                dfs(node.left, 0, c+1, node)
                if parent:
                    dfs(node.right, 1, 1, node)
        
        self.ans = 0
        dfs(root, 0, 0, None)
        dfs(root, 1, 0, None)
        
        return self.ans

