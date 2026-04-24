# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        if curr == None:
            return root

        def recursive(curr):
            if curr.left and curr.right:
                curr.left,curr.right = curr.right,curr.left
                recursive(curr.left)
                recursive(curr.right)
            else:
                return None

            return curr
        
        return recursive(curr)