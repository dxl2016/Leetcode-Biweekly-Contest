# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def pseudoPalindromicPathsHelper(curr_node, temp):
            if curr_node.left is None and curr_node.right is None:
                result.append(temp)
                return
            if curr_node.left:
                pseudoPalindromicPathsHelper(curr_node.left, temp + [curr_node.left.val])
            if curr_node.right:
                pseudoPalindromicPathsHelper(curr_node.right, temp + [curr_node.right.val])

        result = []
        pseudoPalindromicPathsHelper(root, [root.val])
        count = 0
        for res in result:
            t = {}
            a = 0
            for i in res:
                try:
                    t[i] += 1
                except:
                    t[i] = 1
            for k, val in t.items():
                if val % 2 == 1:
                    a += 1
            if a == 1 and len(res) % 2 == 1:
                count += 1
            elif a == 0 and len(res) % 2 == 0:
                count += 1
        return count
        
 
