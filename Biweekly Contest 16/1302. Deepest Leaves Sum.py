# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return
        def deepestLeavesSum(curr_node, height):
            try:
                temp[height] += curr_node.val
            except:
                temp[height] = curr_node.val
            
            if curr_node.left is not None:  
                deepestLeavesSum(curr_node.left, height+1)
            if curr_node.right is not None:  
                deepestLeavesSum(curr_node.right, height+1)
        
        
        temp = {}
        deepestLeavesSum(root, 0)
        tmp = sorted(temp.items(), key=lambda x:x[0])
        
        return tmp[-1][1]

