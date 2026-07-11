# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def bfs(node): 
            nonlocal res
            if node is None: 
                return 
            
            
            queue = deque([root])
            while queue: 
                level_size = len(queue)
                lastLevelled = []
                for n in range(level_size): 
                    nodelist = queue.popleft()
                    if nodelist.left: 
                        queue.append(nodelist.left)
                    if nodelist.right: 
                        queue.append(nodelist.right)
                    if n == level_size - 1: 
                        res.append(nodelist.val)
                    
            
        bfs(root)
        return res



        