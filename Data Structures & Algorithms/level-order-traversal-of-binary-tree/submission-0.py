# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        finallist = [] 
        def bfs(node): 
            queue = deque([root])
            
            while queue:
                levels = []
                for _ in range (len(queue)): 
                    nodelist  = queue.popleft()
                    if nodelist: 
                        levels.append(nodelist.val)
                        queue.append(nodelist.left)
                        queue.append(nodelist.right)
                if levels: 
                    finallist.append(levels)
        bfs(root)

        return finallist 
                         


                

        