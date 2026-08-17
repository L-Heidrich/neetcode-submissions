# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        diff = 0

        def dfs(node):
            nonlocal diff 

            if node == None: 
                return 0
            
            L = dfs(node.left)
            R = dfs(node.right)

            diff = max(diff, abs(L-R)) 

            return 1 + max(L,R)

        dfs(root)

        if diff > 1: 
            return False
        else:
            return True
    
