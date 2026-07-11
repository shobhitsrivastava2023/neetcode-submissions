# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthcounter = 0 
        val = 0 
        def dfs(node):
            nonlocal kthcounter
            nonlocal val  
            if node is None: 
                return 
            
            dfs(node.left)
            kthcounter += 1
            if kthcounter == k: 
                val = node.val
            
            dfs(node.right)
        dfs(root)
        return val
        