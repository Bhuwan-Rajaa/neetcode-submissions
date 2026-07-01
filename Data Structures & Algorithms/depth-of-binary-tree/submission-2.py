# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root,depth):
            if root == None:
                return depth
            
            depthL = dfs(root.left, depth)
            depthR = dfs(root.left, depth)

            return 1+ max(depthL, depthR)

        
        if root:
            return dfs(root,1) 
        else:
            return 0