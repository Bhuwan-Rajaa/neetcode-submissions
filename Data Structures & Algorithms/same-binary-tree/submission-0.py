# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def issame(p,q):
            if not p and not q:
                return True
            if p and q and p.val != q.val:
                return False
            else:
                return issame(p.left,q.left) and issame(p.right,q.right)

        return issame(p,q)