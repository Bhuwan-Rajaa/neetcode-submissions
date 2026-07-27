# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        def dn(root,val):
            if not root:
                return root

            if val<root.val:
                root.left = dn(root.left, val)
            elif val>root.val:
                root.right = dn(root.right,val)
            
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                
                cur = root.left

                while cur.right:
                    cur = cur.right
                
                root.val = cur.val

                root.left = dn(root.left,cur.val)
            return root

        return dn(root,val)