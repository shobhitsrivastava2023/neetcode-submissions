# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        depth = 0
        def bfs(node):
            nonlocal depth 
            if node is None: 
                return 
            queue = deque([node])
            while queue:
                depth += 1 
                levels = len(queue)
                for  _ in range(levels): 
                    node = queue.popleft()
                     
                    if node: 
                        if node.left: 
                            queue.append(node.left)
                        if node.right: 
                            queue.append(node.right)
                
        bfs(root)
        return depth
                    

                
            
        