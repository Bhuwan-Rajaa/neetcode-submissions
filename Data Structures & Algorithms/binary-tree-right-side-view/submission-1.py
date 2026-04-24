# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        depthr = depthl = 0
        rootr = rootl = root

        while rootr:
            res.append(rootr.val)
            rootr = rootr.right
            depthr+=1

        while rootl:
            if depthl>depthr:
                res.append(rootl.val)
            rootl = rootl.left
            depthl +=1

        return res