# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        def goodNodesHelper(curr_node, curr_max):
            if curr_node is None:
                return
            if curr_node.val >= curr_max:
                curr_max = curr_node.val
                self.count += 1
            goodNodesHelper(curr_node.left, curr_max)
            goodNodesHelper(curr_node.right, curr_max)
            return self.count
        
        return goodNodesHelper(root, root.val)
