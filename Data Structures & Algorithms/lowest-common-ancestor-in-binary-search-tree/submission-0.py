# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        anstr = root
        def dfs(node): 
            nonlocal anstr 
            if node is None: 
                return 
            if node.val < p.val and node.val < q.val: 
                dfs(node.right)
            elif (node.val > p.val and node.val > q.val): 
                dfs(node.left)
            else: 
                anstr = node
                return 
        
        dfs(root)
        return anstr


        